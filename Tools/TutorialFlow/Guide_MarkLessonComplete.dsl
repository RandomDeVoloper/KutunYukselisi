(fn MarkLessonComplete (LessonOrder) (if (== LessonOrder (Variables|Default|GetNextLessonOrder)) (Variables|Default|SetNextLessonOrder (+ (Variables|Default|GetNextLessonOrder) 1))))

