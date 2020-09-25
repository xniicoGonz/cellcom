class QueryToList():
    @staticmethod
<<<<<<< HEAD
    def queryall_admin_to_list(query_result):
        list_data = []
        for row in query_result:
            aux_dict = {}
            aux_dict["email"] = row.email
            aux_dict["name"] = row.name
            aux_dict["lastname"] = row.lastname
            aux_dict["identificationCard"] = row.identificationCard
            aux_dict["phone"] = row.phone
            aux_dict["address"] = row.address
            aux_dict["email"] = row.email
            aux_dict["password"] = row.password
            aux_dict["rol"] = row.rol
        return list_data
=======
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
>>>>>>> 1957080... fase final del proyecto
