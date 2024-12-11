from scrapmoveis import ScrapMoveis
from makecsv import MakeCsv

csv = MakeCsv()
csv.new_csv()
for i in range(50):
    apartments = ScrapMoveis(f"https://www.zapimoveis.com.br/aluguel/imoveis/pr+curitiba/?__ab=sup-hl-pl:newC,exp-aa-test:control,super-high:new,off-no-hl:new,pos-zap:new,new-rec:b,zapproppos:control,ltroffline:ltr&transacao=aluguel&onde=,Paran%C3%A1,Curitiba,,,,,city,BR%3EParana%3ENULL%3ECuritiba,-25.426899,-49.265198,&pagina={i + 1}")
    values = apartments.get_values()
    csv.write_scv(values)
