(fn RefreshGuide ()
 (Widget|SetText(Text) (Variables|WBP_TutorialControls|GetControlsText) (Utilities|String|Append (Utilities|String|Append (Utilities|String|Append (Utilities|String|Append (Utilities|String|Append (Utilities|String|Append (Utilities|String|Append "" (select (Variables|Default|GetLearnGrab) "[Sol fare basılı]  Nesneyi tut
" "")) (select (Variables|Default|GetLearnRelease) "[Sol fareyi bırak]  Serbest bırak
" "")) (select (Variables|Default|GetLearnScale) "[Tekerlek]  Boyut değiştir
" "")) (select (Variables|Default|GetLearnPin) "[TAB]  Havada sabitle
" "")) (select (Variables|Default|GetLearnMount) "[G]  Uçan kılıca bin
" "")) (select (Variables|Default|GetLearnSword) "[Sağ fare]  Kılıcı çek / fırlat
" "")) (select (Variables|Default|GetLearnThrow) "[Sol fare tıkla]  Fırlat" "")))
 (if (or (or (or (or (or (or (or false (Variables|Default|GetLearnGrab)) (Variables|Default|GetLearnRelease)) (Variables|Default|GetLearnScale)) (Variables|Default|GetLearnPin)) (Variables|Default|GetLearnMount)) (Variables|Default|GetLearnSword)) (Variables|Default|GetLearnThrow)) (Widget|SetVisibility (Variables|WBP_TutorialControls|GetControlsPanel) "HitTestInvisible") (else (Widget|SetVisibility (Variables|WBP_TutorialControls|GetControlsPanel) "Collapsed")))
 (if (Variables|Default|GetLearnMount) (Widget|SetVisibility (Variables|WBP_TutorialControls|GetControlsFooter) "HitTestInvisible") (else (Widget|SetVisibility (Variables|WBP_TutorialControls|GetControlsFooter) "Collapsed"))))

