import requests
from bs4 import BeautifulSoup

def preco_echodot_simples():
    # Usando site de comparação de preços (mais estável)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
    }
    url = "https://www.amazon.com.br/s?k=echo+dot&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2UXFU4U5FY68V&sprefix=echo+dot%2Caps%2C191&ref=nb_sb_noss_1"
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar primeiro resultado
        # Buscar span que está dentro de h2 com aquela classe
        produto = soup.select_one('h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span')
        # produto = soup.find('span', class_='a-size-base-plus')
        preco = soup.find('span', class_='a-price-whole')
        
        if preco:
            # print(f"📱 {produto.text.strip()}")
            print(f"💰 R$ {preco.text.strip()}")
        else:
            print("🔍 Produto não encontrado")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

preco_echodot_simples()