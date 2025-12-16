from database.DB_connect import DBConnect
from  model.interazione import Interazione
from model.cromosoma import Cromosoma

class DAO:

    @staticmethod
    def read_cromosoma():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT distinct (cromosoma)
                FROM gene
                WHERE cromosoma <> 0
                """

        cursor.execute(query)

        for row in cursor:
            cromosoma = Cromosoma(
                row['id'],
                row['funzione'],
                row['cromosoma'])
            result.append(cromosoma)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_interazione():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select g1.cromosoma as cromosoma_1, g2.cromosoma as cromosoma_2, id_gene1 as gene_1, id_gene2 as gene_2, SUM(correlazione) as Correlazione
                from gene as g1, gene as g2, interazione as i
                where g1.id = i.id_gene1 and g2.id = id_gene2
                and g1.cromosoma <> g2.cromosoma
                and g1.cromosoma <> 0
                and g2.cromosoma <> 0
                group by g1.cromosoma, g2.cromosoma, id_gene1, id_gene2
                """

        cursor.execute(query)

        for row in cursor:
            interazione = Interazione(
                row['cromosoma_1'],
                row['cromosoma_2'],
                row['gene_1'],
                row['gene_2'],
                row['Correlazione'])
            result.append(interazione)

        cursor.close()
        conn.close()
        return result