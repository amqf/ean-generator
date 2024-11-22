# Criar o pacote

Crie o pacote .deb usando o comando dpkg-deb:
```
dpkg-deb --build ean-generator
Isso gerará um arquivo chamado ean-generator.deb no diretório atual.
```

# Testar o pacote

Para instalar o pacote e testar:
```
sudo dpkg -i ean-generator.deb
```

Agora, você pode executar o comando ean-generator no terminal para gerar códigos EAN-13.
