import argparse
import json
import csv
from pathlib import Path

import pandas as pd


class ConcertCatalogue:
    catalogue_df_cols = ["date", "concert_name", "start_time", "end_time",  # 0-3
                         "piece_name", "piece_year_start", "piece_year_end",  # 4-6
                         "composer_name", "composer_year_birth", "composer_year_death",  # 7-9
                         "arranger_name", "opus_number", "item_number",  # 10-12
                         "movements", "performers", "instruments"]  # 13-14

    @staticmethod
    def _list2string(list1, use_json_string=False):
        # transforms a list of string into a string with semicolon separators between items
        # optionally takes in a second list (performers, instruments) and join each item pair with underscore (_)
        if use_json_string:
            return json.dumps(list1, ensure_ascii=False) if list1 else ""
        else:
            return " -- ".join(list1) if list1 else ""

    def __init__(self, json_outputs_dir):
        self.json_outputs_dir = Path(json_outputs_dir) if isinstance(json_outputs_dir, str) else json_outputs_dir
        self.catalogue_dir = Path("generated_catalogues") / f"{self.json_outputs_dir.stem}_catalogue"
        if not self.catalogue_dir.exists():
            self.catalogue_dir.mkdir()
        self.unprocessed_catalogue = self._get_unprocessed_catalogue(self.catalogue_dir / "catalogue_unprocessed.json")

    def _get_unprocessed_catalogue(self, catalogue_fpath):
        if not catalogue_fpath.exists():
            catalogue = {}
            for fpath in self.json_outputs_dir.glob('*.json'):
                with open(fpath) as f:
                    concert_json = json.load(f)
                concert_id = concert_json["date"].replace("-", "")
                if concert_id in list(catalogue.keys()):
                    # if there had been two concerts on the same day
                    concert_id += "a"
                catalogue[concert_id] = concert_json

            with open(catalogue_fpath, "w", encoding="utf-8") as f_obj:
                json.dump(catalogue, f_obj)

        else:
            with open(catalogue_fpath) as f:
                catalogue = json.load(f)

        return catalogue

    def save_catalogue_as_df(self, catalogue):
        all_pieces = []
        for concert_id, concert in catalogue.items():
            concert_info = [concert_id] + [concert[col] for col in self.catalogue_df_cols[:4]]
            for piece in concert["list_of_pieces"]:
                piece_info = concert_info.copy()
                piece_info += [piece[col] for col in self.catalogue_df_cols[4:13]]
                piece_info += [self._list2string(piece["movements"])]
                # performers column
                piece_info += [self._list2string([f"{perf_inst['performer_name']} ({perf_inst['performer_instrument']})"
                                                  for perf_inst in piece["performers"]])]
                # instruments column
                piece_info += [self._list2string([x['performer_instrument'] for x in piece["performers"]])]

                all_pieces.append(piece_info)

        df = pd.DataFrame(all_pieces, columns=["concert_id"] + self.catalogue_df_cols)

        df.to_csv(self.catalogue_dir / "catalogue_unprocessed.tsv", index=False, encoding="utf-8", sep="\t", quoting=csv.QUOTE_NONE, escapechar="\\")
        return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_outputs_dir', type=str, required=True)
    args = parser.parse_args()

    concert_catalogue = ConcertCatalogue(args.json_outputs_dir)
    df = concert_catalogue.save_catalogue_as_df(concert_catalogue.unprocessed_catalogue)
    print("Catalogue exported")
