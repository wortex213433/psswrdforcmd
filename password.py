import random
import string
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Language:
    def __init__(self):
        self.current = 'en'
        self.texts = {
            'en': {
                'welcome': '\033[1;34mWelcome to Password Generator!\033[0m',
                'menu': '\n\033[1;32mMain Menu:\033[0m\n1. Generate Password\n2. Settings\n3. Coded By\n4. Exit',
                'enter_choice': 'Enter your choice: ',
                'invalid_choice': '\033[1;31mInvalid choice. Try again.\033[0m',
                'gen_pass': '\033[1;33mPassword Generation:\033[0m',
                'length': 'Enter password length (8-50): ',
                'invalid_length': '\033[1;31mLength must be between 8 and 50.\033[0m',
                'uppercase': 'Include uppercase letters? (y/n): ',
                'lowercase': 'Include lowercase letters? (y/n): ',
                'digits': 'Include digits? (y/n): ',
                'special': 'Include special characters? (y/n): ',
                'security_level': 'Security level (low/medium/high): ',
                'invalid_level': '\033[1;31mInvalid level. Choose low, medium, or high.\033[0m',
                'generating': 'Generating password...',
                'password': '\033[1;32mYour password:\033[0m {}',
                'another': 'Generate another? (y/n): ',
                'settings_menu': '\n\033[1;32mSettings:\033[0m\n1. Change Language\n2. Back',
                'lang_choice': 'Choose language (en/tr/es/fr): ',
                'invalid_lang': '\033[1;31mInvalid language. Choose en, tr, es, or fr.\033[0m',
                'credits': '\n\033[1;35mCoded By:\033[0m\nMade by wortex213433\nA simple yet powerful password generator with multi-language support.',
                'goodbye': '\033[1;34mThank u for trying!\033[0m'
            },
            'tr': {
                'welcome': '\033[1;34mŞifre Oluşturucuya Hoş Geldin!\033[0m',
                'menu': '\n\033[1;32mAna Menü:\033[0m\n1. Şifre Oluştur\n2. Ayarlar\n3. Coded By\n4. Çıkış',
                'enter_choice': 'Seçiminizi girin: ',
                'invalid_choice': '\033[1;31mGeçersiz seçim. Tekrar deneyin.\033[0m',
                'gen_pass': '\033[1;33mŞifre Oluşturma:\033[0m',
                'length': 'Şifre uzunluğunu girin (8-50): ',
                'invalid_length': '\033[1;31mUzunluk 8 ile 50 arasında olmalı.\033[0m',
                'uppercase': 'Büyük harf olsun mu? (e/h): ',
                'lowercase': 'Küçük harf olsun mu? (e/h): ',
                'digits': 'Rakam olsun mu? (e/h): ',
                'special': 'Özel karakter olsun mu? (e/h): ',
                'security_level': 'Güvenlik seviyesi (düşük/orta/yüksek): ',
                'invalid_level': '\033[1;31mGeçersiz seviye. Düşük, orta veya yüksek seviyelerinden birini seçin.\033[0m',
                'generating': 'Şifreniz oluşturuluyor...',
                'password': '\033[1;32mŞifreniz:\033[0m {}',
                'another': 'Başka bir tane daha oluşturmak ister misiniz? (e/h): ',
                'settings_menu': '\n\033[1;32mAyarlar:\033[0m\n1. Dil Değiştir\n2. Geri',
                'lang_choice': 'Dil seçin (en/tr/es/fr): ',
                'invalid_lang': '\033[1;31mGeçersiz dil. En, tr, es veya fr seçin.\033[0m',
                'credits': '\n\033[1;35mCoded By:\033[0m\nMade by wortex213433\nBasit ama etkili bir random şifre oluşturucu.',
                'goodbye': '\033[1;34mDenediğiniz için teşekkürler!\033[0m'
            },
            'es': {
                'welcome': '\033[1;34m¡Bienvenido al Generador de Contraseñas!\033[0m',
                'menu': '\n\033[1;32mMenú Principal:\033[0m\n1. Generar Contraseña\n2. Configuraciones\n3. Coded By\n4. Salir',
                'enter_choice': 'Ingrese su elección: ',
                'invalid_choice': '\033[1;31mElección inválida. Intente de nuevo.\033[0m',
                'gen_pass': '\033[1;33mGeneración de Contraseña:\033[0m',
                'length': 'Ingrese la longitud de la contraseña (8-50): ',
                'invalid_length': '\033[1;31mLa longitud debe estar entre 8 y 50.\033[0m',
                'uppercase': '¿Incluir letras mayúsculas? (s/n): ',
                'lowercase': '¿Incluir letras minúsculas? (s/n): ',
                'digits': '¿Incluir dígitos? (s/n): ',
                'special': '¿Incluir caracteres especiales? (s/n): ',
                'security_level': 'Nivel de seguridad (bajo/medio/alto): ',
                'invalid_level': '\033[1;31mNivel inválido. Elija bajo, medio o alto.\033[0m',
                'generating': 'Generando contraseña...',
                'password': '\033[1;32mSu contraseña:\033[0m {}',
                'another': '¿Generar otra? (s/n): ',
                'settings_menu': '\n\033[1;32mConfiguraciones:\033[0m\n1. Cambiar Idioma\n2. Volver',
                'lang_choice': 'Elija idioma (en/tr/es/fr): ',
                'invalid_lang': '\033[1;31mIdioma inválido. Elija en, tr, es o fr.\033[0m',
                'credits': '\n\033[1;35mCoded By:\033[0m\nMade by wortex213433\nUn generador de contraseñas simple pero poderoso con soporte multilingüe.',
                'goodbye': '\033[1;34m¡Adiós!\033[0m'
            },
            'fr': {
                'welcome': '\033[1;34mBienvenue au Générateur de Mot de Passe!\033[0m',
                'menu': '\n\033[1;32mMenu Principal:\033[0m\n1. Générer un Mot de Passe\n2. Paramètres\n3. Coded By\n4. Quitter',
                'enter_choice': 'Entrez votre choix: ',
                'invalid_choice': '\033[1;31mChoix invalide. Réessayez.\033[0m',
                'gen_pass': '\033[1;33mGénération de Mot de Passe:\033[0m',
                'length': 'Entrez la longueur du mot de passe (8-50): ',
                'invalid_length': '\033[1;31mLa longueur doit être entre 8 et 50.\033[0m',
                'uppercase': 'Inclure des lettres majuscules? (o/n): ',
                'lowercase': 'Inclure des lettres minuscules? (o/n): ',
                'digits': 'Inclure des chiffres? (o/n): ',
                'special': 'Inclure des caractères spéciaux? (o/n): ',
                'security_level': 'Niveau de sécurité (bas/moyen/haut): ',
                'invalid_level': '\033[1;31mNiveau invalide. Choisissez bas, moyen ou haut.\033[0m',
                'generating': 'Génération du mot de passe...',
                'password': '\033[1;32mVotre mot de passe:\033[0m {}',
                'another': 'Générer un autre? (o/n): ',
                'settings_menu': '\n\033[1;32mParamètres:\033[0m\n1. Changer la Langue\n2. Retour',
                'lang_choice': 'Choisissez la langue (en/tr/es/fr): ',
                'invalid_lang': '\033[1;31mLangue invalide. Choisissez en, tr, es ou fr.\033[0m',
                'credits': '\n\033[1;35mCoded By:\033[0m\nMade by wortex213433\nUn générateur de mot de passe simple mais puissant avec support multilingue.',
                'goodbye': '\033[1;34mAu revoir!\033[0m'
            }
        }

    def get(self, key):
        return self.texts[self.current][key]

lang = Language()

def generate_password(length, use_upper, use_lower, use_digits, use_special, level):
    pool = ''
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_special:
        pool += string.punctuation

    if level == 'high':
        if length < 12:
            length = 12
        if not (use_upper and use_lower and use_digits and use_special):
            use_upper = use_lower = use_digits = use_special = True
            pool = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    elif level == 'medium':
        if not (use_upper or use_lower or use_digits or use_special):
            pool = string.ascii_letters + string.digits
    elif level == 'low':
        if not pool:
            pool = string.ascii_letters

    if not pool:
        return None

    return ''.join(random.choice(pool) for _ in range(length))

def get_yes_responses():
    if lang.current == 'tr':
        return ['e', 'y']
    elif lang.current == 'es':
        return ['s', 'y']
    elif lang.current == 'fr':
        return ['o', 'y']
    else:
        return ['y']

def settings_menu():
    while True:
        clear_screen()
        print(lang.get('settings_menu'))
        choice = input(lang.get('enter_choice'))
        if choice == '1':
            new_lang = input(lang.get('lang_choice')).lower()
            if new_lang in ['en', 'tr', 'es', 'fr']:
                lang.current = new_lang
            else:
                print(lang.get('invalid_lang'))
                input('Press Enter...')
        elif choice == '2':
            break
        else:
            print(lang.get('invalid_choice'))
            input('Press Enter...')

def main():
    clear_screen()
    print(lang.get('welcome'))

    while True:
        print(lang.get('menu'))
        choice = input(lang.get('enter_choice'))

        if choice == '1':
            clear_screen()
            print(lang.get('gen_pass'))

            while True:
                try:
                    length = int(input(lang.get('length')))
                    if not 8 <= length <= 50:
                        print(lang.get('invalid_length'))
                        continue
                except ValueError:
                    print(lang.get('invalid_length'))
                    continue

                yes_responses = get_yes_responses()
                use_upper = input(lang.get('uppercase')).lower() in yes_responses
                use_lower = input(lang.get('lowercase')).lower() in yes_responses
                use_digits = input(lang.get('digits')).lower() in yes_responses
                use_special = input(lang.get('special')).lower() in yes_responses

                level = input(lang.get('security_level')).lower()
                level_map = {
                    'en': {'low': 'low', 'medium': 'medium', 'high': 'high'},
                    'tr': {'düşük': 'low', 'orta': 'medium', 'yüksek': 'high'},
                    'es': {'bajo': 'low', 'medio': 'medium', 'alto': 'high'},
                    'fr': {'bas': 'low', 'moyen': 'medium', 'haut': 'high'}
                }
                mapped_level = level_map.get(lang.current, {}).get(level)
                if not mapped_level:
                    print(lang.get('invalid_level'))
                    continue
                level = mapped_level

                print(lang.get('generating'))
                password = generate_password(length, use_upper, use_lower, use_digits, use_special, level)
                if password:
                    print(lang.get('password').format(password))
                else:
                    print('\033[1;31mNo character types selected. Using defaults.\033[0m')
                    password = generate_password(length, True, True, True, False, 'medium')
                    print(lang.get('password').format(password))

                another = input(lang.get('another')).lower() in yes_responses
                if not another:
                    break

        elif choice == '2':
            settings_menu()

        elif choice == '3':
            clear_screen()
            print(lang.get('credits'))
            input('Press Enter to return...')

        elif choice == '4':
            clear_screen()
            print(lang.get('goodbye'))
            sys.exit(0)

        else:
            print(lang.get('invalid_choice'))
            input('Press Enter...')

if __name__ == '__main__':
    main()
