from database_utils import DatabaseUtils
import random


class WordAnalyser:
    def __init__(self):
        self.lexique_db = DatabaseUtils("databases/lexique.db")

    def lemme(self, word):
        return self.lexique_db.select("lexique", "lemme", "ortho='" + word + "'")

    def phon(self, phon):
        return self.lexique_db.select("lexique", "ortho", "phon lIKE '%" + phon + "%'")

    def find_word(self, word):
        return self.lexique_db.select("lexique", where="ortho='" + word + "'")

    def pick_word(self,diff=2):
        return random.choice(self.lexique_db.select("lexique", where="ortho=lemme "
                                                                     "AND (freqlivres+freqfilms2)/2 > 0.1 "
                                                                     "AND length(phon)>"+str(diff)))
