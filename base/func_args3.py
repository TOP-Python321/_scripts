def test_function(pos_arg1,
                  pos_arg2,
                  /,
                  pos_key_arg1,
                  pos_key_arg2='default',
                  *,
                  key_arg1,
                  key_arg2):
    pass


test_function('arg1', 
              'arg2', 
              'arg3', 
              'arg4',
              key_arg1='arg5', 
              key_arg2='arg6')

test_function('arg1', 
              'arg2', 
              pos_key_arg1='arg3', 
              pos_key_arg2='arg4',
              key_arg1='arg5', 
              key_arg2='arg6')

test_function('arg1', 
              'arg2',
              pos_key_arg1='arg3', 
              key_arg1='arg5', 
              key_arg2='arg6')

test_function('arg1', 
              'arg2',
              key_arg2='arg6',
              key_arg1='arg5', 
              pos_key_arg1='arg3') 

