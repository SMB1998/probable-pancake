import contextvars

cvar_volunteer = contextvars.ContextVar("localStorage_data",
                              default = False)

cvar_admin = contextvars.ContextVar("localStorage_data",
                              default = False)