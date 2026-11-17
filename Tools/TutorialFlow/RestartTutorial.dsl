(fn RestartTutorial ()
 (Variables|Default|SetTutorialStep 0)
 (Variables|Default|SetTutorialElapsed 0.0)
 (Variables|Default|SetTutorialRetryCount (+ (Variables|Default|GetTutorialRetryCount) 1))
 (Variables|Default|SetInitialSwordState (Class|BPTelekinezi|GetSwordonHand (Variables|Default|GetTutorialPlayer)))
 (CallFunction|RefreshTutorial))

