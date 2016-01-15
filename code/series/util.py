import os


def poster_path(instance, filename):
    """
    Given a Series instance and file name return path and file name to be saved in

    If the instance is not None then the filename will be {pk}.{ext}
    """
    path = 'series/poster'
    root, ext = os.path.splitext(filename)
    # get filename
    if instance:
        filename = '{}{}'.format(instance.id, ext)
    # return the whole path to the file
    return os.path.join(path, filename)
