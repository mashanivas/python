class class1:

      def __init__(self, name, cls, grade, eligible_for_award):

         self.name = name
         self.cls = cls
         self.grade = grade
         self.eligible_for_award = eligible_for_award

      def award_check(self):
         if self.grade >= 3.8:
              return True
         else:
              return False
