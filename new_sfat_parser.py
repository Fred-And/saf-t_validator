from xml.dom import minidom

def noe_index_calculation(doc,desired_type):
    tagName = []
    #doc = minidom.parse(path_to_doc)
    document = doc.getElementsByTagName("NumberOfEntries")
    for i in document:
        tagName.append(i.parentNode.tagName)
    try:
        index = tagName.index(desired_type)
        return index
    except:
        return "NIL"

def invoice_resume(path_to_doc):
    doc = minidom.parse(path_to_doc)
    entry_index = noe_index_calculation(doc,"SalesInvoices")
    invoices = doc.getElementsByTagName("Invoice")
    if  isinstance(entry_index, (int)):
        n_of_invoice_entries = doc.getElementsByTagName("NumberOfEntries")[entry_index].childNodes[0].data
        total_credit_declared = doc.getElementsByTagName("TotalCredit")[entry_index].childNodes[0].data
        invoice_len = invoices.length
        total_credit_calculated = []
        net_total_list = []
        taxes_total_list = []
        
        
        for i in invoices:
            gross_total = i.getElementsByTagName('GrossTotal')[0].childNodes[0].data
            net_total =  i.getElementsByTagName('NetTotal')[0].childNodes[0].data
            tax_payable = i.getElementsByTagName('TaxPayable')[0].childNodes[0].data
            total_credit_calculated.append(float(gross_total))
            net_total_list.append(float(net_total))
            taxes_total_list.append(float(tax_payable))
        
        val1 = int(n_of_invoice_entries) == int(invoice_len)
        val2 = float(total_credit_declared) ==  float(sum(net_total_list))
        val3 = round(float(sum(total_credit_calculated)),2)== round(float((sum(net_total_list))+(round(sum(taxes_total_list),2))),2)
        
        if val1 and  val2 and val3 == True:
            validation = 1
        else:
            validation = 0
        
        result = {
            "number_of_invoice_dec":n_of_invoice_entries,
            "number_of_invoice_calc":invoice_len,
            "total_invoices_declared":total_credit_declared,
            "total_invoices_calculated":round(sum(net_total_list),2),
            "total_taxes_calculated":round(sum(taxes_total_list),2),
            "total_dec_invoices_plus_tax":round(sum(total_credit_calculated),2),
            "total_calc_invoices_plus_tax":round((sum(net_total_list))+(round(sum(taxes_total_list),2)),2),
            "validation": validation
        }
        return result
    else:
        return {}

def receipt_resume(path_to_doc):
    doc = minidom.parse(path_to_doc)
    entry_index = noe_index_calculation(doc,"Payments")
    receipts = doc.getElementsByTagName("Payment")
    if isinstance(entry_index, (int)):
        n_of_receipt_entries = doc.getElementsByTagName("NumberOfEntries")[entry_index].childNodes[0].data
        total_credit_declared = doc.getElementsByTagName("TotalCredit")[entry_index].childNodes[0].data
        receipts_len = receipts.length
        total_credit_calculated = []
        net_total_list = []
        taxes_total_list = []
        
        for i in receipts:
            gross_total = i.getElementsByTagName('GrossTotal')[0].childNodes[0].data
            net_total =  i.getElementsByTagName('NetTotal')[0].childNodes[0].data
            tax_payable = i.getElementsByTagName('TaxPayable')[0].childNodes[0].data
            total_credit_calculated.append(float(gross_total))
            net_total_list.append(float(net_total))
            taxes_total_list.append(float(tax_payable))
        
        val1 = int(n_of_receipt_entries) == int(receipts_len)
        val2 = round(float(total_credit_declared),0) ==  round(float(sum(net_total_list)),0)
        val3 = round(float(sum(total_credit_calculated)),2)== round(float((sum(net_total_list))+(round(sum(taxes_total_list),2))),2)
        
        if val1 and  val2 and val3 == True:
            validation = 1
        else:
            validation = 0
        
        result = {
            "number_of_receipt_dec":n_of_receipt_entries,
            "number_of_receipt_calc":receipts_len,
            "total_receipts_declared":total_credit_declared,
            "total_receipts_calculated":round(sum(net_total_list),2),
            "total_taxes_calculated":round(sum(taxes_total_list),2),
            "total_dec_receipt_plus_tax":round(sum(total_credit_calculated),2),
            "total_calc_receipt_plus_tax":round((sum(net_total_list))+(sum(taxes_total_list)),2),
            "validation": validation
        }
        return result
    else:
        return {}

def working_documents_resume(path_to_doc):
    doc = minidom.parse(path_to_doc)
    entry_index = noe_index_calculation(doc,"WorkingDocuments")
    working_documents = doc.getElementsByTagName("WorkDocument")
    if isinstance(entry_index, (int)):
        n_of_wd_entries = doc.getElementsByTagName("NumberOfEntries")[entry_index].childNodes[0].data
        total_credit_declared = doc.getElementsByTagName("TotalCredit")[entry_index].childNodes[0].data
        wd_len = working_documents.length
        total_credit_calculated = []
        net_total_list = []
        taxes_total_list = []
        
        for i in working_documents:
            gross_total = i.getElementsByTagName('GrossTotal')[0].childNodes[0].data
            net_total =  i.getElementsByTagName('NetTotal')[0].childNodes[0].data
            tax_payable = i.getElementsByTagName('TaxPayable')[0].childNodes[0].data
            total_credit_calculated.append(float(gross_total))
            net_total_list.append(float(net_total))
            taxes_total_list.append(float(tax_payable))
        
        val1 = int(n_of_wd_entries) == int(wd_len)
        val2 = round(float(total_credit_declared),0) ==  round(float(sum(net_total_list)),0)
        val3 = float(sum(total_credit_calculated))== float((sum(net_total_list))+(round(sum(taxes_total_list),2)))
        
        if val1 and  val2 and val3 == True:
            validation = 1
        else:
            validation = 0
        
        result = {
            "number_of_wd_dec":n_of_wd_entries,
            "number_of_wd_calc":wd_len,
            "total_wds_declared":total_credit_declared,
            "total_wds_calculated":sum(net_total_list),
            "total_taxes_calculated":round(sum(taxes_total_list),2),
            "total_dec_wd_plus_tax":round(sum(total_credit_calculated),2),
            "total_calc_wd_plus_tax":round((sum(net_total_list))+(sum(taxes_total_list)),2),
            "validation": validation
        }
        return result
    else:
        return {}
    
    
    


if __name__ == "__main__":
    receipt_resume('/Users/fredericoandrade/Documents/IX/SCB/299/SAF-T_07_2023.xml')
    #my_test = receipt_resume('/Users/fredericoandrade/Documents/IX/SCB/287/SAF-T_7_2023.xml')
    #print(my_test)