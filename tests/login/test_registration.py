# from fixtures.constants import Errors
# from fixtures.models.register import RegisterData
#
#
# class TestRegistration:
#     def test_registration_with_valid_data(self, app, user_data):
#         """
#         Steps:
#         1. Open register page
#         2. Add valid data
#         3. Check result
#         """
#         app.open_register_page()
#         data = RegisterData.random()
#         app.register.add_new_user(data)
#         assert 1 == 1
#
#     def test_registration_with_empty_name(self, app, user_data):
#         """
#         Steps:
#         1. Open register page
#         2. Add data with empty name
#         3. Check result
#         """
#         app.open_register_page()
#         data = RegisterData.random()
#         setattr(data, "name", None)
#         app.register.add_new_user(data)
#         error = app.register.get_error_name()
#         assert error == Errors.ERROR_FIRST_NAME, "Check error first name"
