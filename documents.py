from abc import ABC, abstractmethod


# =========================
# Интерфейс документа
# =========================

class Document(ABC):

    @abstractmethod
    def open(self):
        pass


# =========================
# Конкретные документы
# =========================

class Report(Document):

    def open(self):
        print("Opening Report document...")


class Resume(Document):

    def open(self):
        print("Opening Resume document...")


class Letter(Document):

    def open(self):
        print("Opening Letter document...")


# НОВЫЙ тип документа (Счет / Invoice)
class Invoice(Document):

    def open(self):
        print("Opening Invoice document...")


# =========================
# Создатель (Базовый класс фабрики)
# =========================

class DocumentCreator(ABC):

    @abstractmethod
    def create_document(self):
        pass


# =========================
# Конкретные создатели
# =========================

class ReportCreator(DocumentCreator):

    def create_document(self):
        return Report()


class ResumeCreator(DocumentCreator):

    def create_document(self):
        return Resume()


class LetterCreator(DocumentCreator):

    def create_document(self):
        return Letter()


class InvoiceCreator(DocumentCreator):

    def create_document(self):
        return Invoice()
