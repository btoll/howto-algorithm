import ipdb


#def longest_absolute_path(s):
#    i = 0
#    resource = 0
#    depth = 0
#    paths = []
#    max_path = 0
#
#    while i < len(s):
#        if s[i] == "\n":
#            part = s[resource:i]
#            depth = 0
#            i += 1
#            while s[i + depth] == "\t":
#                depth += 1
#            if "." in part:
#                if len(part) < max_path:
#                    paths.pop()
#                else:
#                    max_path = max(max_path, len(part))
#            i += depth
#            resource = i
#            paths.append(part)
#        i += 1
#
#    paths.append(s[resource:])
#    return paths, max_path


def longest_absolute_path(s):
    parts = s.split("\n")
    max_path = 0
    fs = {}

    for part in parts:
        level = 0

        while part[level] == "\t" and level < len(part):
            level += 1

        path_len = len(part) if level == 0 else fs[level - 1] + len(part[level:]) + 1

        if "." in part:
            max_path = max(max_path, path_len)
        else:
            fs[level] = path_len

    return max_path


s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(longest_absolute_path(s))
