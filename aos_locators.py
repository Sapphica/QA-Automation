from faker import Faker
fake = Faker(locale='en_CA')
# --------------locators section-----------------
app = 'Moodle'
safe_pay_user = 'spuser'
safe_pay_pass ='Pass123'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = '\xa0Advantage Shopping'
test = ' '

# ------------------data section-----------------
first_name = fake.first_name()
last_name = fake.last_name()
new_username = f'{last_name}{fake.pyint(11, 999)}'.lower()
new_password = fake.password()
email = f'{first_name}{fake.pyint(11, 999)}@{fake.free_email_domain()}'
city = fake.city()
phone = fake.phone_number()[:13]
postal = fake.postcode()
province = fake.province()[:10]
address = fake.street_address()

list_reg = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage', 'cityRegisterPage',
'state_/_province_/_regionRegisterPage', 'postal_codeRegisterPage', 'addressRegisterPage']
list_vars = [new_username, email, new_password, new_password, first_name, last_name, phone, city,
province, postal, address]