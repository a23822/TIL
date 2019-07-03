``` terminal
git branch feature/merge_1
➜  git-basic-education git:(master) git branch feature/merge_2
➜  git-basic-education git:(master) git branch
➜  git-basic-education git:(master) git checkout feature/merge_1
Switched to branch 'feature/merge_1'
➜  git-basic-education git:(feature/merge_1) echo >> newfile.md
➜  git-basic-education git:(feature/merge_1) ✗ git add .
➜  git-basic-education git:(feature/merge_1) ✗ git status
On branch feature/merge_1
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   newfile.md

➜  git-basic-education git:(feature/merge_1) ✗ git commit -m "merge_1 커밋"
[feature/merge_1 6656460] merge_1 커밋
 1 file changed, 1 insertion(+)
 create mode 100644 newfile.md
➜  git-basic-education git:(feature/merge_1) git checkout feature/merge_2
Switched to branch 'feature/merge_2'
➜  git-basic-education git:(feature/merge_2) echo >> newfile.md
➜  git-basic-education git:(feature/merge_2) ✗ git add .
➜  git-basic-education git:(feature/merge_2) ✗ git status
On branch feature/merge_2
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   newfile.md

➜  git-basic-education git:(feature/merge_2) ✗ git commit -m "merge_2 커밋"
[feature/merge_2 7f99852] merge_2 커밋
 1 file changed, 1 insertion(+)
 create mode 100644 newfile.md
➜  git-basic-education git:(feature/merge_2) git checkout feature/merge_1
Switched to branch 'feature/merge_1'
➜  git-basic-education git:(feature/merge_1) git merge feature/merge_2
CONFLICT (add/add): Merge conflict in newfile.md
Auto-merging newfile.md
Automatic merge failed; fix conflicts and then commit the result.
➜  git-basic-education git:(feature/merge_1) ✗ git merge --abort
➜  git-basic-education git:(feature/merge_1) git checkout feature/merge_2
Switched to branch 'feature/merge_2'
➜  git-basic-education git:(feature/merge_2) ls
README.md  newfile.md
➜  git-basic-education git:(feature/merge_2) git add .
➜  git-basic-education git:(feature/merge_2) ✗ git status
On branch feature/merge_2
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	renamed:    newfile.md -> newfile2.md

➜  git-basic-education git:(feature/merge_2) ✗ git commit -m "conflict 해결"
[feature/merge_2 89b0777] conflict 해결
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename newfile.md => newfile2.md (100%)
➜  git-basic-education git:(feature/merge_2) git checkout feature/merge_1
Switched to branch 'feature/merge_1'
➜  git-basic-education git:(feature/merge_1) git merge feature/merge_2
Merge made by the 'recursive' strategy.
 newfile2.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 newfile2.md


```