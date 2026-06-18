from programme_structure import *

DEMONSTRATION_EXAMPLE_INPUTS_FPATHS = [
    "data/in_context_example_inputs/prog8March2024.txt",
    "data/in_context_example_inputs/12Nov18prog.txt",
]

DEMONSTRATION_EXAMPLE_OUTPUTS = [
    # prog8March2024
    Concert(concert_name='Shakespeare around the World or a Celebration of the First Folio',
            date='2024-03-08', start_time='7:00pm', end_time='8:00pm',
            list_of_pieces=[
                Piece(piece_name='Piano pieces from Romeo and Juliet',
                      piece_year_start=1937, piece_year_end=None,
                      composer_name='Sergei Prokofiev', composer_year_birth=1891, composer_year_death=1953,
                      arranger_name=None, opus_number='Op. 75', item_number=None,
                      movements=['Street scene', 'Romeo and Juliet before parting', 'Dance of the girls with lilies'],
                      performers=[Performer(performer_name='R[anonymised]', performer_instrument='piano')]),
                Piece(piece_name='Ständchen (‘Horch, horch, die Lerch’)', piece_year_start=1826, piece_year_end=None,
                      composer_name='Franz Schubert', composer_year_birth=1797, composer_year_death=1828,
                      arranger_name=None, opus_number='D 889', item_number=None, movements=None,
                      performers=[Performer(performer_name='J[anonymised]', performer_instrument='bass'),
                                  Performer(performer_name='R[anonymised]', performer_instrument='piano')]),
                Piece(piece_name='An Silvia', piece_year_start=1826, piece_year_end=None, composer_name='Franz Schubert',
                      composer_year_birth=1797, composer_year_death=1828, arranger_name=None, opus_number='Op. 106',
                      item_number='No. 4', movements=None, performers=[
                        Performer(performer_name='J[anonymised]', performer_instrument='bass'),
                        Performer(performer_name='R[anonymised]', performer_instrument='piano')]),
                Piece(piece_name='If music be the food of love', piece_year_start=1692,
                      piece_year_end=None, composer_name='Henry Purcell', composer_year_birth=1659,
                      composer_year_death=1695, arranger_name=None, opus_number='Z 379', item_number=None,
                      movements=None, performers=[
                        Performer(performer_name='R[anonymised]', performer_instrument='soprano'),
                        Performer(performer_name='Z[anonymised]', performer_instrument='alto'),
                        Performer(performer_name='R[anonymised]', performer_instrument='piano')]),
                Piece(piece_name='Where the bee sucks', piece_year_start=1746, piece_year_end=None,
                      composer_name='Thomas Augustine Arne', composer_year_birth=1710, composer_year_death=1778,
                      arranger_name=None, opus_number=None, item_number=None, movements=None, performers=[
                        Performer(performer_name='R[anonymised]', performer_instrument='soprano'),
                        Performer(performer_name='Z[anonymised]', performer_instrument='alto'),
                        Performer(performer_name='R[anonymised]', performer_instrument='piano')]),
                Piece(piece_name='‘A boy like that... I have a love’ from West Side Story',
                      piece_year_start=1957, piece_year_end=None, composer_name='Leonard Bernstein',
                      composer_year_birth=1918, composer_year_death=1990, arranger_name=None,
                      opus_number=None, item_number=None, movements=None,
                      performers=[Performer(performer_name='R[anonymised]', performer_instrument='soprano'),
                                  Performer(performer_name='Z[anonymised]', performer_instrument='alto'),
                                  Performer(performer_name='R[anonymised]', performer_instrument='piano')]),
                Piece(piece_name='That time of year thou may\'st in me behold', piece_year_start=2014,
                      piece_year_end=None, composer_name='Roger Beeson', composer_year_birth=1945,
                      composer_year_death=None, arranger_name=None, opus_number=None, item_number=None,
                      movements=None, performers=[
                        Performer(performer_name='R[anonymised]', performer_instrument='soprano'),
                        Performer(performer_name='Z[anonymised]', performer_instrument='alto'),
                        Performer(performer_name='P[anonymised]', performer_instrument='tenor'),
                        Performer(performer_name='J[anonymised]', performer_instrument='bass'),
                        Performer(performer_name='R[anonymised]', performer_instrument='piano')])])
    ,

    # 12Nov18prog
    Concert(concert_name='Joint concert with the Oxford and Cambridge Musical Club',
            date='2018-11-12',
            start_time='7:00pm', end_time=None,
            list_of_pieces=[
                Piece(piece_name='Andante con moto in C minor',
                      piece_year_start=1878, piece_year_end=None,
                      composer_name='Edvard Grieg', composer_year_birth=1843,
                      composer_year_death=1907, arranger_name=None, opus_number=None,
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='D[anonymised]', performer_instrument='violin'),
                          Performer(performer_name='T[anonymised]', performer_instrument='’cello'),
                          Performer(performer_name='G[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='\'Sleep\' from Five Elizabethan Songs',
                      piece_year_start=1920, piece_year_end=None,
                      composer_name='Ivor Gurney', composer_year_birth=1890,
                      composer_year_death=1937, arranger_name=None, opus_number=None,
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='L[anonymised]', performer_instrument='soprano'),
                          Performer(performer_name='N[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='\'Now the Leaves are Falling Fast from On This Island\' from On This Island',
                      piece_year_start=1937, piece_year_end=None,
                      composer_name='Benjamin Britten', composer_year_birth=1913,
                      composer_year_death=1976, arranger_name=None, opus_number='Op.11',
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='L[anonymised]', performer_instrument='soprano'),
                          Performer(performer_name='N[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='\'C\' from Deux poèmes de Louis Aragon',
                      piece_year_start=1943, piece_year_end=None,
                      composer_name='Francis Poulenc', composer_year_birth=1899,
                      composer_year_death=1963, arranger_name=None, opus_number=None,
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='L[anonymised]', performer_instrument='soprano'),
                          Performer(performer_name='N[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='Cello Sonata No.2 in C major',
                      piece_year_start=1935, piece_year_end=None,
                      composer_name='George Enescu', composer_year_birth=1881,
                      composer_year_death=1955, arranger_name=None, opus_number='Op.26',
                      item_number='No.2',
                      movements=['i. Allegro moderato ed amabile'],
                      performers=[
                          Performer(performer_name='T[anonymised]', performer_instrument='\’cello'),
                          Performer(performer_name='P[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='Four Newspaper Announcements',
                      piece_year_start=1926, piece_year_end=None,
                      composer_name='Aleksandr Mosolov', composer_year_birth=1900,
                      composer_year_death=1973, arranger_name=None, opus_number='Op.21',
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='J[anonymised]', performer_instrument='mezzo-soprano'),
                          Performer(performer_name='R[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='2 Woofs',
                      piece_year_start=1947, piece_year_end=None,
                      composer_name='Henry Cowell', composer_year_birth=1897,
                      composer_year_death=1967, arranger_name=None, opus_number=None,
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='C[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='\'Les Chiens de Galata\' from Le rossignol éperdu',
                      piece_year_start=1902, piece_year_end=1910,
                      composer_name='Reynaldo Hahn', composer_year_birth=1874,
                      composer_year_death=1947, arranger_name=None, opus_number='Op.53',
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='C[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='Helford River at Night',
                      piece_year_start=None, piece_year_end=None,
                      composer_name='Anthony Green', composer_year_birth=1946,
                      composer_year_death=None, arranger_name=None, opus_number=None,
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='R[anonymised]', performer_instrument='viola'),
                          Performer(performer_name='C[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='Lachrymae',
                      piece_year_start=1950, piece_year_end=None,
                      composer_name='Benjamin Britten', composer_year_birth=None,
                      composer_year_death=None, arranger_name=None, opus_number='Op.48',
                      item_number=None,
                      movements=None,
                      performers=[
                          Performer(performer_name='R[anonymised]', performer_instrument='viola'),
                          Performer(performer_name='R[anonymised]', performer_instrument='piano')
                      ]
                      ),

                Piece(piece_name='Tango Etudes',
                      piece_year_start=None, piece_year_end=None,
                      composer_name='Astor Piazzolla', composer_year_birth=1921,
                      composer_year_death=1992, arranger_name=None, opus_number=None,
                      item_number='No.3, No.4, No.6',
                      movements=None,
                      performers=[
                          Performer(performer_name='K[anonymised]', performer_instrument='violin')
                      ]
                      )
            ])
]
