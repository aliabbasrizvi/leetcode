class Solution(object):
  def removeSubfolders(self, folders):
    """
    :type folders: List[str]
    :rtype: List[str]
    """
    folders = sorted(folders)
    print folders
    unique_folders = []
    if len(folders) > 0:
      unique_folders.append(folders[0])

    for current_folder in folders:
      for folder in unique_folders:
        if (current_folder + '/').startswith(folder + '/'):
          continue
        else:
          unique_folders.append(current_folder)

    return sorted(list(set(unique_folders)))

s = Solution()
print s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
print s.removeSubfolders(["/a","/a/b/c","/a/b/d"])
print s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])
