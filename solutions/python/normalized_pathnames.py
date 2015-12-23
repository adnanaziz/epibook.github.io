# normalized_pathnames.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys


# @include
def shortest_equivalent_path(path):
    path_names = []  # Uses list as a stack.
    # Special case: starts with '/', which is an absolute path.
    if path[0] == '/':
        path_names.append('/')

    for token in path.split('/'):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        elif token != '.' and token != '':  # Must be a name.
            path_names.append(token)

    result = '/'.join(path_names)
    if result.startswith('//'):  # Avoid starting '//'.
        result = result[1:]
    return result
# @exclude


def main():
    assert shortest_equivalent_path('123/456') == '123/456'
    assert shortest_equivalent_path('/123/456') == '/123/456'
    assert shortest_equivalent_path('usr/lib/../bin/gcc') == 'usr/bin/gcc'
    assert shortest_equivalent_path('./../') == '..'
    assert shortest_equivalent_path('../../local') == '../../local'
    assert shortest_equivalent_path('./.././../local') == '../../local'
    try:
        shortest_equivalent_path('/foo.txt')
    except ValueError as e:
        print(e)
    try:
        shortest_equivalent_path('/..')
    except ValueError as e:
        print(e)
    try:
        shortest_equivalent_path('/cpp_name/bin/')
    except ValueError as e:
        print(e)
    assert (shortest_equivalent_path('scripts//./../scripts/awkscripts/././') ==
            'scripts/awkscripts')
    if len(sys.argv) == 2:
        print(shortest_equivalent_path(sys.argv[1]))


if __name__ == '__main__':
    main()