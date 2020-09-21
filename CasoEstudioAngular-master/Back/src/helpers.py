class QueryToList():
    @staticmethod
    def queryall_bill_to_list(query_result):
        list_data =[]
        for row in query_result:
            aux_dict = {}
            aux_dict["value"] = row.value
            aux_dict["id_bill"] = row.id_bill
            aux_dict["collectionDay"] = row.collectionDay
            aux_dict["customerIdentification "]= row.customerIdentification
            aux_dict["numberLine"] = row.numberLine
        return list_data
