from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    '''
    Комманда для заполнения данными базу данных
    '''
    def handle(self, *args, **options):
        try:
            call_command('loaddata', 'database_data.json')
        except:
            print('Ошибка загрузки данных!')