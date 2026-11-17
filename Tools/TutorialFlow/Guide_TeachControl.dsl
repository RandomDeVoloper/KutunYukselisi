(fn TeachControl (Kind Step)
 (switch int Kind
 (:0 (CallFunction|RefreshGuide))
 (:1 (CallFunction|RefreshGuide))
 (:2 (Variables|Default|SetLearnGrab true) (if (>= Step 1) (Variables|Default|SetLearnRelease true)) (CallFunction|RefreshGuide))
 (:3 (Variables|Default|SetLearnGrab true) (if (>= Step 1) (Variables|Default|SetLearnScale true)) (CallFunction|RefreshGuide))
 (:4 (Variables|Default|SetLearnGrab true) (if (>= Step 1) (Variables|Default|SetLearnPin true)) (CallFunction|RefreshGuide))
 (:5 (Variables|Default|SetLearnMount true) (CallFunction|RefreshGuide))
 (:6 (Variables|Default|SetLearnSword true) (CallFunction|RefreshGuide))
 (:7 (Variables|Default|SetLearnGrab true) (if (>= Step 1) (Variables|Default|SetLearnThrow true)) (CallFunction|RefreshGuide))))

