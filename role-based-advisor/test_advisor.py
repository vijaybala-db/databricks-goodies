from advisor import RoleBasedAdvisor

def test_init():
    myadvisor = RoleBasedAdvisor(role='doctor', language_model='openai')
    assert 'happiness' in myadvisor.user_question

def test_get_llm():
    myadvisor = RoleBasedAdvisor(role='doctor', language_model='openai')
    assert myadvisor.llm is not None

def test_answer_as_role():
    myadvisor = RoleBasedAdvisor(role='doctor', language_model='llamav2')
    answer = myadvisor.answer_as_role('How to improve my wellness?', 'doctor', verbose=True)
    print(answer)
    assert 'wellness' in answer