from selenium import webdriver

# Configuração do Chrome Driver
driver_path = 'caminho/para/o/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=perfil/whatsappweb')
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Acessa o site do WhatsApp Web
driver.get('https://web.whatsapp.com/')