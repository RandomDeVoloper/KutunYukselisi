(fn CompleteTutorial ()
 (if (not (Variables|Default|GetTutorialFinished))
  (Variables|Default|SetTutorialFinished true)
  (Variables|Default|SetTutorialSuccessElapsed 0.0)
  (Utilities|IsValid (Variables|Default|GetTutorialControls)
   (:"Is Valid"
    (Class|WBPTutorialControls|MarkLessonComplete :self (Variables|Default|GetTutorialControls) :LessonOrder (Variables|Default|GetTutorialOrder))
    (CallFunction|RefreshTutorial))
   (:"Is Not Valid" (CallFunction|RefreshTutorial)))))

