class QueryToList():
    @staticmethod
    def queryall_bill_to_list(result_query):
        list_data =[]
        for row in result_query:
            aux_dict = {}
            aux_dict["value"] = row.value
            aux_dict["id_bill"] = row.id_bill
            aux_dict["collectionDay"] = row.collectionDay
            aux_dict["customerIdentification "]= row.customerIdentification
            aux_dict["numberLine"] = row.numberLine
            list_data.append(aux_dict)
        return list_data
