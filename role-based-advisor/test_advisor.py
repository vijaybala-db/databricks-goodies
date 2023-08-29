from advisor import RoleBasedAdvisor

def test_init():
    myadvisor = RoleBasedAdvisor(language_model='openai')
    assert 'happiness' in myadvisor.user_question

def test_get_llm():
    myadvisor = RoleBasedAdvisor(language_model='openai')
    assert myadvisor.llm is not None

def test_answer_as_role():
    myadvisor = RoleBasedAdvisor(language_model='llamav2', config_file_path='/tmp/llamav2_config.json')
    answer = myadvisor.answer_as_role('How to improve my wellness?', 'doctor', verbose=True)
    print(answer)
    assert 'wellness' in answer