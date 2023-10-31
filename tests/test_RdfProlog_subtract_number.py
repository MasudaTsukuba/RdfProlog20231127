"""
test_RdfProlog_subtract_number.py
T. Masuda, 2023/10/30
"""

from src.RdfProlog import RdfProlog, ClassSparqlQuery


def test_answer_question1():
    rdf_prolog = RdfProlog()

    # subtract(3, 1, ?ans)
    my_question = \
        f'SELECT ?ans WHERE {{' \
        f'?s <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s <http://example.org/variable_x> <http://example.org/three> . ' \
        f'?s <http://example.org/variable_y> <http://example.org/one> . ' \
        f'?s <http://example.org/variable_z> ?ans . ' \
        f'}}'
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/two>'


def test_answer_question2():
    rdf_prolog = RdfProlog()

    # subtract(4, 2, ?ans)
    my_question = \
        f'SELECT ?ans WHERE {{ ?s <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s <http://example.org/variable_x> <http://example.org/four> . ' \
        f'?s <http://example.org/variable_y> <http://example.org/two> . ' \
        f'?s <http://example.org/variable_z> ?ans . ' \
        f'}} '
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/two>'


def test_answer_question3():
    rdf_prolog = RdfProlog()

    # # subtract(3, 2, ?ans)
    my_question = \
        f'SELECT ?ans WHERE {{' \
        f'?s <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s <http://example.org/variable_x> <http://example.org/three> . ' \
        f'?s <http://example.org/variable_y> <http://example.org/two> . ' \
        f'?s <http://example.org/variable_z> ?ans . ' \
        f'}}'
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/one>'


def test_answer_question3b():
    rdf_prolog = RdfProlog()

    # subtract(5, 2, ?z), next(?z, ?ans)
    my_question = \
        f'SELECT ?ans WHERE {{' \
        f'?s1 <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s1 <http://example.org/variable_x> <http://example.org/five> . ' \
        f'?s1 <http://example.org/variable_y> <http://example.org/two> . ' \
        f'?s1 <http://example.org/variable_z> ?z . ' \
        f'?s2 <http://example.org/operation> <http://example.org/next_number> . ' \
        f'?s2 <http://example.org/variable_x> ?z . ' \
        f'?s2 <http://example.org/variable_y> ?ans . ' \
        f'}}'
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/four>'


def test_answer_question4():
    rdf_prolog = RdfProlog()

    # subtract(5, ?ans, 2)
    my_question = \
        f'SELECT ?ans WHERE {{' \
        f'?s <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s <http://example.org/variable_x> <http://example.org/five> . ' \
        f'?s <http://example.org/variable_y> ?ans . ' \
        f'?s <http://example.org/variable_z> <http://example.org/two> . ' \
        f'}}'
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/three>'


def test_answer_complex_question1():
    rdf_prolog = RdfProlog()

    # subtract(5, 2, ?z), next(?z, ?ans)
    my_question = \
        f'SELECT ?ans WHERE {{' \
        f'?s1 <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s1 <http://example.org/variable_x> <http://example.org/five> . ' \
        f'?s1 <http://example.org/variable_y> <http://example.org/two> . ' \
        f'?s1 <http://example.org/variable_z> ?z . ' \
        f'?s2 <http://example.org/operation> <http://example.org/next_number> . ' \
        f'?s2 <http://example.org/variable_x> ?z . ' \
        f'?s2 <http://example.org/variable_y> ?ans . ' \
        f'}}'
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)  # ###################
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/four>'


def test_answer_complex_question2():
    rdf_prolog = RdfProlog()

    # subtract(3, 2, ?z), add(?z, 2, ?ans)
    my_question = \
        my_question = \
        f'SELECT ?ans WHERE {{' \
        f'?s1 <http://example.org/operation> <http://example.org/subtract_number> . ' \
        f'?s1 <http://example.org/variable_x> <http://example.org/three> . ' \
        f'?s1 <http://example.org/variable_y> <http://example.org/two> . ' \
        f'?s1 <http://example.org/variable_z> ?z . ' \
        f'?s2 <http://example.org/operation> <http://example.org/add_number> . ' \
        f'?s2 <http://example.org/variable_x> ?z . ' \
        f'?s2 <http://example.org/variable_y> <http://example.org/two> . ' \
        f'?s2 <http://example.org/variable_z> ?ans . ' \
        f'}}'
    my_sparql_query = ClassSparqlQuery().set(my_question).build_rule()
    resolve_bindings = rdf_prolog.answer_complex_question(my_sparql_query)  # ###################
    assert resolve_bindings[0]['?ans'] == f'<http://example.org/three>'