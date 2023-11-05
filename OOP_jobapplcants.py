class JobApplicants:
    def __init__(self,name,age,experience):
        self.name = name 
        self.age = age
        self.experience = experience
    
    def display_info(self):
        print(f'ชื่อ: {self.name}')
        print(f'อายุ: {self.age}')
        print(f'ประสบการณ์การทำงาน: {self.experience} ปี')

    def apply_for_job(self, position):
        print(f'{self.name} สมัครตำแหน่งงาน: {position}')

class ExperiencedApplicant(JobApplicants):
    def interview(self, feedback):
        print(f'{self.name} ผ่านการสัมภาษณ์งาน')

#สร้างวัตถุ JobApplicants
alc1 = JobApplicants('Boy', 25, 2)
alc2 = JobApplicants('Parn', 29, 6)

# สร้างวัตถุ ExperiencedApplicant
experienced_applicant = ExperiencedApplicant("Bob", 35, 10)

#แสดงข้อมูลผู้สมัคร
print('ข้อมูลผู้สมัคร:')
alc1.display_info()

print('\nข้อมูลผู้สมัคร:')
alc2.display_info()

# ตำแหน่งงานและการสัมภาษณ์
print('\n-----------')
alc1.apply_for_job('บัญชี')
alc2.apply_for_job('โปรแกรมเมอร์')

print('\n-----------')

experienced_applicant.apply_for_job('โฆษณา')
experienced_applicant.interview()