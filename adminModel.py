from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.type_user == 1
    form_excluded_columns = ('users_id')
    column_exclude_list = ('passw')