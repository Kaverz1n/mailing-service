# СЕРВИС УПРАВЛЕНИЯ РАССЫЛКАМИ

## ОПИСАНИЕ ПРОЕКТА

Сервис управления рассылками — это современное веб-приложение, разработанное с использованием фреймворка **Django**
и языка программирования **Python**, целью которого является облегчение и автоматизация процесса рассылки
персонализированных
электронных писем клиентам. Данный проект предоставляет пользователям мощные инструменты для создания и управления
рассылками, а также управления клиентской базой данных. С его помощью пользователи могут легко и эффективно
взаимодействовать с аудиторией, обеспечивая высокий уровень персонализации и контроля.

## ОСОБЕННОСТИ ПРОЕКТА

1. **Регистрация и аутентификация**: Пользователи могут безопасно и просто зарегистрироваться на платформе,
   гарантированно подтверждая свою уникальность через электронную почту. Это обеспечивает надежную идентификацию
   пользователей и сохранность их данных. Для обеспечения безопасности и уникальности аккаунтов, после регистрации
   отправляется подтверждение на указанный email, который пользователь должен подтвердить, прежде чем получить полный
   доступ к платформе.
2. **Создание персонализированных рассылок**: Платформа предоставляет пользователям удобные инструменты для создания
   персонализированных рассылок. Пользователи сами выбирают, кому, когда и с каким содержанием будут отправлены
   электронные письма. В любой момент пользователь в праве удалить или завершить собственную рассылку.
3. **Работа с клиентской базой**: Платформа предоставляет удобные инструменты для эффективного управления клиентской
   базой.
   Пользователи могут добавлять, редактировать и обновлять информацию о клиентах, обеспечивая актуальность данных.
4. **Модерация и контроль**: Команда модераторов внимательно следит за качеством и соответствием контента на
   платформе. Модераторы проверяют рассылки и гарантируют, что они соответствуют тематике и не содержат недопустимого
   контента.
5. **Блог и информационные материалы**: Блог-модератор регулярно обновляет платформу интересными и полезными статьями,
   следит за актуальностью контента и обогащаем платформу информацией, которая поможет быть в курсе последних
   тенденций.

## ТРЕБОВАНИЯ К НАСТРОЙКЕ И ЗАПУСКУ ПРОЕКТА

### НАСТРОЙКА ПРОЕКТА

1. **Активация виртуального окружения**: Создайте и активируйте виртуальное окружение с помощью команды в вашем
   терминале. Пример для
   **macOS/Linux**:

   ```commandline
   source venv/Scripts/activate
   ```

2. **Установка зависимостей**: Установите зависимости, указанные в **requirements.txt**, с помощью команды:

   ```commandline
   pip install -r requirements.txt
   ```

3. **Создание файла .env**: Создайте файл с именем **.env** в корневой директории вашего проекта. В файле **.env**
   заполните
   все нижепредставленные переменные окружения:

   ```text
   SECRET_KEY=
   DEBUG=
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   DATABASE_PORT=
   LANGUAGE_CODE=
   TIME_ZONE=
   MEDIA_URL=
   MEDIA_ROOT=
   EMAIL_PORT=
   EMAIL_USE_SSL=
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   CACHE_ENABLED=
   REDIS_LOCATION=
   ```

4. **Применение миграций**: Примените миграции для обновления вашей базы данных согласно изменениям в приложении с
   помощью команды:

   ```commandline
   python manage.py migrate
   ```

5. **Заполнение базы данных**: Откройте терминал и выполните следующие команды для очистки таблицы **ContentType** и
   заполнения базы данных:

   ```commandline
   python manage.py shell
   ```

   В интерактивной оболочке Python выполните:

   ```python
   from django.contrib.contenttypes.models import ContentType
   
   ContentType.objects.all().delete()
   ```

   Затем введите команду, которая заполнит базу данных данными, необходимымы для вашего проекта:

   ```commandline
   python manage.py fill
   ```
6. **Создание суперпользователя**: Создайте суперпользователя, который будет иметь доступ к административной панели
   Django, с помощью команды:
   ```commandline
   python manage.py csu
   ```
7. **Активация Crontab**: Необходимо активировать **Crontab** на вашем сервере для выполнение регулярных задач в
   автоматическом режиме с помощью следующей команды:
   ```commandline
   sudo service cron start
   ```
8. **Запуск Crontab**: Необходимо запустить **Crontab** в проекте. Для этого введите команду в консоль:
   ```commandline
   python manage.py crontab add
   ```
9. **Активация Redis**: Необходимо активировать **Redis** на вашем сервере для кэширования и хранения данных с помощью
   следующей команды:
   ```commandline
   sudo service redis-server start
   ```
10. **Предварительная отчистка кэша**: Откройте терминал и выполните следующую команду для отчистки кэша:
   ```commandline
   python manage.py clear_cache
   ```
   > Во время разработки, после добавления или изменения данных, рекомендуется выполнить отчистку кэша
   > для обновления результатов.

### ЗАПУСК ПРОЕКТА

1. **Запуск проекта**: Для запуска Django проекта необходимо прописать комманду:
   ```commandline
   python manage.py runserver
   ```
2. **Использование проекта**: Откройте веб-браузер и перейдите по адресу, указанному в консоли
   (обычно **http://127.0.0.1:8000/**).
   > Проведите тестирование различных функциональностей вашего проекта, чтобы удостовериться, что они работают как
   ожидалось.

## РАСПРЕДЕЛЕНИЕ РОЛЕЙ

1. **Пользователь (г. service_users)**: Пользователи, работающие с рассылками, представляют собой обычных
   зарегистрированных
   пользователей платформы. Пользователи могут создавать рассылки, определяя получателей, текст сообщения и
   настройки отправки.
   Для удобства работы с рассылками, у каждого пользователя есть личный кабинет, где можно редактировать и удалять
   рассылки, а также отслеживать их статус и время следующей отправки.
   > Группа **service_users** присваивается любому пользователю после регистрации
2. **Менеджер (г. manager)**: Менеджеры, также называемые модераторами, назначаются администраторами. Их основная
   задача - контроль за созданными рассылками пользователями и обеспечение их соответствия
   правилам и качеству. Менеджеры могут удалять или завершать рассылки. Так же блокировать некоторых пользователей.
   > Группу **manager** необходимо устанавливать через административную панель Django
3. **Блог-Менеджер (г. blog_manager)**: Блог-модераторы также назначаются администраторами. Их обязанность - создавать и
   управлять контентом блога, предоставляя полезные статьи и материалы для
   пользователей.
   Блог-модераторы следят за актуальностью и качеством контента на платформе, участвуют в формировании образа сообщества
   и
   информационной политики.
   > Группу **blog_manager** необходимо устанавливать через административную панель Django

#### УСТАНОВКА РОЛИ ПОЛЬЗОВАТЕЛЮ

1. **Авторизация в административной панели**: Войдите в административную панель вашего Django проекта,
   перейдя по URL-адресу, обычно **http://127.0.0.1:8000/admin/**, и введите свои учетные данные администратора.
2. **Навигация к пользователям**: В административной панели найдите раздел, связанный с управлением пользователями.
3. **Выбор пользователя:** Найдите пользователя, которому вы хотите присвоить определенную группу, и выберите его,
   нажав на его данные.
4. **Редактирование пользователя**: В открывшейся странице редактирования пользователя вы должны найти раздел "Группы"
   который позволяет управлять группами пользователя.
5. **Выбор группы**: В этом разделе вы увидите список доступных групп. Выберите группу, которую вы хотите присвоить
   пользователю.
6. **Сохранение изменений**: После выбора группы, убедитесь, что сохраните изменения, нажав на соответствующую кнопку
   "Сохранить".

## ТЕХНОЛОГИИ

- **Используемые технологии**: Проект выполнен на фреймворке **Django**, используя язык
  программирования **Python**. Для хранения данных применяется база данных, совместимая с **Django** - **PostgreSQL**.

- **Интерфейс**: Для веб-интерфейса применяется шаблонизация с использованием **HTML** и **CSS**. Для улучшения
  пользовательского опыта использован **Bootstrap**.

## СВЯЗЬ

Если у вас возникли вопросы, предложения или потребность в поддержке, не стесняйтесь связаться со мной. Я готов помочь
Вам с вашим проектом и ответить на все Ваши вопросы. Вы можете связаться со мной по следующим контактам:

- Электронная почта: **dima.captan@yandex.ru**
- Telegram: **@Kaverz1n**

## БЛАГОДАРНОСТЬ

Я хотел бы выразить свою искреннюю благодарность вам за использование проекта и за проявленное доверие. Ваше участие и
поддержка являются неоценимыми для меня и для развития моего приложения.

# СПАСИБО ЗА ВАШЕ ВРЕМЯ И УЧАСТИЕ В ЖИЗНИ ПРОЕКТА