import streamlit as st
from new_sfat_parser import invoice_resume, receipt_resume, working_documents_resume

#st.image()
st.title('SAF-T Validator')
st.caption('By: InvoiceXpress')

# File Uploader
uploaded_doc = st.file_uploader(label= "Faça aqui o upload do SAF-T", type= 'xml',accept_multiple_files= False,)
st.sidebar.warning("This is not an official source for SAF-T validation and status, always double check  and validate yout SAF-T with the Portuguese Tax Authority")
# Check if a file was uploaded
if uploaded_doc is not None:
    st.write("SAF-T carregado com sucesso!")
    
    selected_option = st.selectbox(
        "Selecioine o que deseja extrair de informações deste ficheiro",
        options=['Invoices',
                 'Receipts',
                 'Working Documents'])
    
    if selected_option == 'Invoices':
        invoice_resume = invoice_resume(uploaded_doc)
        
        if not invoice_resume:
            st.warning('This SAF-T does not contain any invoice.')
        
        else:
        
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f""" 
                            \n1. Number of declared Invoices: **{invoice_resume['number_of_invoice_dec']}**
                            \n2. Total of Declared Credit: **{invoice_resume['total_invoices_declared']}**€
                            \n3. Declared Invoices + Tax: **{invoice_resume['total_dec_invoices_plus_tax']}**€
                            """)
                
            with col2:
                st.markdown(f"""
                            \n1. Number of calculated Invoices: **{invoice_resume['number_of_invoice_calc']}**
                            \n2. Total of Calculated Credit: **{invoice_resume['total_invoices_calculated']}**€
                            \n3. Calculated Invoices + Taxes: **{invoice_resume['total_calc_invoices_plus_tax']}**€
                            \n4. Total of Calculated Taxes: **{invoice_resume['total_taxes_calculated']}**€
                            """)
            
            if invoice_resume['validation'] == 1:
                #st.balloons()
                st.success("All the values are correct")
            else:
                st.error("There's an Error in the SAF-T")
            
            
        
    elif selected_option == 'Receipts':
        receipt_resume = receipt_resume(uploaded_doc)
        
        if not invoice_resume:
            st.warning('This SAF-T does not contain any Receipt.')
        
        else:
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f""" 
                            \n1. Number of declared Receipts: **{receipt_resume['number_of_receipt_dec']}**
                            \n2. Total of Declared Credit: **{receipt_resume['total_receipts_declared']}**€
                            \n3. Declared Receipts + Tax: **{receipt_resume['total_dec_receipt_plus_tax']}**€
                            """)
                
            with col2:
                st.markdown(f"""
                            \n1. Number of calculated Receipts: **{receipt_resume['number_of_receipt_calc']}**
                            \n2. Total of Calculated Credit: **{receipt_resume['total_receipts_calculated']}**€
                            \n3. Calculated Receipts + Taxes: **{receipt_resume['total_calc_receipt_plus_tax']}**€
                            \n4. Total of Calculated Taxes: **{receipt_resume['total_taxes_calculated']}**€
                            """)
            
            if receipt_resume['validation'] == 1:
                #st.balloons()
                st.success("All the values are correct")
            else:
                st.error("There's an Error in the SAF-T")
        
            
    elif selected_option == 'Working Documents':
        working_documents_resume = working_documents_resume(uploaded_doc)
        
        if not working_documents_resume:
            st.warning('This SAF-T does not contain any WorkingDocument.')
        
        else:
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown(f""" 
                            \n1. Number of declared Work Docs: **{working_documents_resume['number_of_wd_dec']}**
                            \n2. Total of Declared Credit: **{working_documents_resume['total_wds_declared']}**€
                            \n3. Declared Work Docs + Tax: **{working_documents_resume['total_dec_wd_plus_tax']}**€
                            """)
                
            with col2:
                st.markdown(f"""
                            \n1. Number of calculated Work Docs: **{working_documents_resume['number_of_wd_calc']}**
                            \n2. Total of Calculated Credit: **{working_documents_resume['total_wds_calculated']}**€
                            \n3. Calculated Work Docs + Taxes: **{working_documents_resume['total_calc_wd_plus_tax']}**€
                            \n4. Total of Calculated Taxes: **{working_documents_resume['total_taxes_calculated']}**€
                            """)
            
            if working_documents_resume['validation'] == 1:
                #st.balloons()
                st.success("All the values are correct")
            else:
                st.error("There's an Error in the SAF-T")