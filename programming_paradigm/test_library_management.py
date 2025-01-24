import unittest
from  library_management import Book, Library

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        """Configuration des données avant chaque test"""
        # Création de livres pour les tests
        self.book1 = Book("Python Basics", "John Doe")
        self.book2 = Book("Learn Java", "Jane Smith")

        # Création d'une bibliothèque
        self.library = Library()
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        """Test de l'ajout de livres dans la bibliothèque"""
        self.assertEqual(len(self.library._Library__books), 2)  # La bibliothèque contient 2 livres
        self.library.add_book(Book("C++ Programming", "Alice Walker"))
        self.assertEqual(len(self.library._Library__books), 3)  # Après ajout, il y a 3 livres

    def test_check_out_book(self):
        """Test de l'emprunt d'un livre"""
        self.library.check_out_book("Python Basics")
        self.assertTrue(self.book1.is_checked_out())  # Le livre est emprunté
        self.assertFalse(self.book2.is_checked_out())  # Le deuxième livre n'est pas emprunté

    def test_check_out_nonexistent_book(self):
        """Test de l'emprunt d'un livre qui n'existe pas"""
        self.library.check_out_book("Nonexistent Book")
        # Aucun livre ne doit être marqué comme emprunté
        self.assertFalse(self.book1.is_checked_out())
        self.assertFalse(self.book2.is_checked_out())

    def test_return_book(self):
        """Test du retour d'un livre"""
        self.library.check_out_book("Python Basics")  # Emprunter d'abord le livre
        self.library.return_book("Python Basics")    # Retourner le livre
        self.assertFalse(self.book1.is_checked_out())  # Le livre est maintenant disponible

    def test_return_nonexistent_book(self):
        """Test du retour d'un livre qui n'existe pas"""
        self.library.return_book("Nonexistent Book")  # Ne doit pas causer d'erreur
        self.assertFalse(self.book1.is_checked_out())
        self.assertFalse(self.book2.is_checked_out())

    def test_list_available_books(self):
        """Test de la liste des livres disponibles"""
        # Emprunter un livre
        self.library.check_out_book("Python Basics")
        
        # Vérifier que seulement le deuxième livre est disponible
        available_books = [
            book.get_title()
            for book in self.library._Library__books
            if not book.is_checked_out()
        ]
        self.assertEqual(available_books, ["Learn Java"])

if __name__ == "__main__":
    unittest.main()