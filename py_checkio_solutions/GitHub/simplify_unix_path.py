#!/usr/bin/env checkio --domain=py run simplify-unix-path
def simplify_path(path):
    """
        simplifying a given path
    """
    dir_list = [dir for dir in filter(lambda name: name, path.split('/'))]
    pref = '/' if path.startswith('/') else ''
    res = ''
    while dir_list:
        dir = dir_list.pop(0)
        if dir == '..':
            to = res.rfind('/')
            if res:
                res = res[:to] if to >= 0 else (f'../{dir}' if res == '..' else '')
            elif not res and not pref:
                res += dir
        elif dir == '.':
            continue
        else:
            res += f'{"" if res in ("", "/") else "/"}{dir}'
    res = pref + res
    if not res:
        res = '.'
    print(res)
    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert simplify_path(".././..") == "../.."

    # you can't go deeper than root folder
    assert simplify_path('/for/../..') == '/'
    assert simplify_path('/for/../../no/..') == '/'
    # last slash is not important
    assert simplify_path('/a/') == '/a'

    # double slash can be united in one
    assert simplify_path('/a//b/c') == '/a/b/c'

    # double dot - go to previous folder
    assert simplify_path('dir/fol/../no') == 'dir/no'
    assert simplify_path('dir/fol/../../no') == 'no'

    # one dot means current dir
    assert simplify_path('/a/b/./ci') == '/a/b/ci'
    assert simplify_path('vi/..') == '.'
    assert simplify_path('./.') == '.'

    # not all double-dots can be simplyfied in related path
    assert simplify_path('for/../..') == '..'
    assert simplify_path('../foo') == '../foo'


    print('Simply enough! Let\'s check it now!!')
