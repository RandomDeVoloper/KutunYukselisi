(fn AdvanceTutorialStep ()
 (Variables|Default|SetTutorialStep 1)
 (Variables|Default|SetTutorialElapsed 0.0)
 (Class|WBPTutorialControls|TeachControl :self (Variables|Default|GetTutorialControls) :Kind (Variables|Default|GetTutorialKind) :Step 1)
 (CallFunction|RefreshTutorial))

