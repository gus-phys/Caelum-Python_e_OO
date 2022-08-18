
def teste_args_kwargs(**kwargs):
    for i, arg in enumerate(kwargs):
        print('arg{} -> chave: {} e valor: {}'.format(i+1, arg, kwargs[arg]))