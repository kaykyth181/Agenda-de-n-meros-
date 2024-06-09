import re
import textwrap
agenda = {}


agenda["João"] = "1199998888"
agenda["Maria"] = "1234567890"
agenda["Pedro"] = "1312345678"


    	
while True:
    

    
    escolham = input(" \n consultar \n deletar\n adicionar \n alterar \n parar \n\n escolha uma dessas opções\n")
    escolhas = escolham.lower()
    escolha = re.sub(r"\s+", "", escolhas)

    if escolha == "consultar" or escolha == "c":
        for k, v in agenda.items():
            print(f"{k}: {v}\n")
    
    
    elif escolha == "deletar":
        
        
     
        deletare = input("\nescreva qual deletar: \n")
        deletar = re.sub(r"\s+", "", deletare)
        
        del agenda[deletar]
       
    elif escolha == "adicionar":
       pessoam = input("\nqual o nome? \n")
       pessoa = pessoam.strip()
       nume = input("\nqual o numero? \n")
       num = nume.strip()
       agenda[pessoa] = num 
        
       
    
    
    elif escolha == "alterar":
        
        qual = input(" \nqual alterar?\n\n numero\n nome\n")
        if qual == "numero":
            
            
            alterare = input("\nescreva qual alterar: \n")
            alterar = re.sub(r"\s+", "", alterare)
            vale = input("\nqual vai ser o novo número? \n")
            val = re.sub(r"\s+", "", vale)
            agenda[alterar] = val
        
        else: 
            pessoa = input("\nqual o nome que quer alterar? \n")
            pessoam = re.sub(r"\s+", "", pessoa) 
            pessoanovo = input("\nqual o novo nome?\n")
            num = agenda[pessoam] 
            del agenda[pessoam]
            
            agenda[pessoanovo] = num
        
    elif escolha == "parar":
        break  
        
    else: 
        print("\nEscolha inválida\n")