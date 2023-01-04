from playwright.sync_api import sync_playwright
import time
import time 
from plyer import notification
import yaml

# +
# direct="C:/Users/Diego/AppData/Local/Google/Chrome/User Data"

direct="C:/Users/Diego/AppData/Local/Mozilla/Firefox/Profiles/ow35cx67.default"
# -

# Carga el archivo YAML
with open('data.yaml', 'r') as f:
    credenciales = yaml.safe_load(f)
# Accede a tus credenciales
usuario = credenciales['usuario']
contrasena = credenciales['contrasena']

# +
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    browser = p.firefox.launch_persistent_context(channel="firefox"
                                                                  ,headless=False,
                                                                  user_data_dir=direct)
    page = browser.new_page()
    page.goto("https://app.iess.gob.ec/iess-gestion-agendamiento-citas-medicas-web/login/login.jsf")
    time.sleep(3)
    page.locator("input[data-p-rmsg='Ingrese su usuario.']").type(usuario, delay=100);
    time.sleep(2)
    page.locator("input[id='formLogin:keyPassword']").type(contrasena, delay=200);    
    
    time.sleep(3)
    page.locator("button").click()
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    page.locator("button[id='formularioAgendamientoCitasMedicas:btnContinuar']").click()
    # page.evaluate("""async () => { document.querySelector("button").click() }""")
    page.wait_for_load_state("networkidle")
    time.sleep(3)
#     cdu=page.evaluate("""async () => {
    
#         var cedu=document.getElementsByTagName("td")[5].innerHTML
        
#         function sleep(ms) {
#           return new Promise(resolve => setTimeout(resolve, ms));
#         }

#         async function delayedGreeting() {
#           document.getElementById('formularioAgendamientoCitasMedicas:cmbProvincia_label').click()
#           await sleep(1000);
#           document.getElementById('formularioAgendamientoCitasMedicas:cmbProvincia_1').click()
#           await sleep(1000);
#           document.getElementById('formularioAgendamientoCitasMedicas:cmbCanton_label').click()
#           await sleep(1000);
#           document.getElementById('formularioAgendamientoCitasMedicas:cmbCanton_3').click()
#           await sleep(1000);
#           document.getElementById('formularioAgendamientoCitasMedicas:cmbArea_label').click()
#           await sleep(1000);
#           document.getElementById('formularioAgendamientoCitasMedicas:cmbArea_7').click()
#           await sleep(1000);
#           document.getElementById('formularioAgendamientoCitasMedicas:btnDisponibilidad').click()
#         }
#         delayedGreeting();
#     return cedu
#     }""")
    time.sleep(30)
    # print(cdu)
    browser.close()

# +
# notification.notify(

# title="Alerta",
# message=" Existen Cosnsultas disponibles",
#     # timeout=100
# )

# +
# from plyer import notification

# notification.notify(
#     title='Título de la notificación',
#     message='Mensaje de la notificación',
#     app_name='Nombre de tu aplicación',
#     timeout=10,  # Duración de la notificación en segundos
#     # app_icon='sound.wav'  # Archivo de sonido a utilizar
# )
