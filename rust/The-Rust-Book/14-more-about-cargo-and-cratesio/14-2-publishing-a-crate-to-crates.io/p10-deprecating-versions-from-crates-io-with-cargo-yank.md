# Deprecating Versions from Crates.io with cargo yank

Although you can't remove previous verions of a crate, you can prevent any future projects from
adding them as a new dependency. This is useful when a crate version is broken for one reason or
another. In such situations, Cargo supports *yanking* a crate version.

Yanking a verion prevents new projects from depending on that version while allowing all existing
projects that depend on it to continue. Essentially, a yank means that all projects with a *Cargo.lock*
will not break, and any future *Cargo.lock* files generated will not use the yanked version.

To yank a version of a crate, in the directory of the crate that you've previously published, run **cargo**
**yank** and specify which version you want to yank. For example, if we've published a crate named
**guessing_game** version 1.0.1 and we want to yank it, in the project directory for **guessing_game**
we'd run:

$ cargo yank --vers 1.0.1
    Updating crates.io index
        Yank guessing_game@1.0.1


By adding --undo to the command, you can also undo a yank and allow projects to start depending
on a versoin again:

$ cargo yank --vers 1.0.1 --undo
    Updating crates.io index
      Unyank guessing_game@1.0.1


A yank *does not* delete any code. It cannot, for example, delete accidentally uploaded secrets. If that
happens, you must reset those secrets immediately.
