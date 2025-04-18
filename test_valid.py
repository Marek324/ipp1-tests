from tests.utils_tests import run_valid_test


def test_minimal1():
    input = """
        class Main:Object{run[|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_minimal2():
    input = """
        class Main:Integer{run[|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Integer">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_almost_minimal1():
    input = """
        class A:Object{}
        class Main:A{run[|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="A" parent="Object" />
            <class name="Main" parent="A">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_almost_minimal2():
    input = """
        class A:Object{}
        class B:A{}
        class Main:B{run[|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="A" parent="Object" />
            <class name="B" parent="A" />
            <class name="Main" parent="B">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_description1():
    input = """
        class Main:Object{run[|]} "comment"
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="comment">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_description2():
    input = """
        class Main:Object{run[|]} "comment\nnewline"
        """
    exp_output = """
    <?xml version="1.0" encoding="UTF-8"?>
    <program language="SOL25" description="comment&#10;newline">
        <class name="Main" parent="Object">
            <method selector="run">
                <block arity="0" />
            </method>
        </class>
    </program>
    """
    run_valid_test(input, exp_output)

def test_description3():
    input = """
        class Main:Object{run[|]} "comment" "another"
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="comment">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_description4():
    input = """
        class Main:Object{run[|]} "comment\n\nnewline"
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="comment&#10;&#10;newline">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_multiple_classes():
    input = """
        class Main : Object {run [|]}
        class Main2 : Object {run [|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
            <class name="Main2" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_multiple_methods():
    input = """
        class Main : Object {
            run [|]
            run2 [|]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
                <method selector="run2">
                    <block arity="0" />
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_multiple_parameters():
    input = """
        class Main : Object {
            run [|]
            self:from:nil: [:x :y :z |]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0" />
                </method>
                <method selector="self:from:nil:">
                    <block arity="3">
                        <parameter order="1" name="x" />
                        <parameter order="2" name="y" />
                        <parameter order="3" name="z" />
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_multiple_assign():
    input = """
        class Main : Object {
            run [| 
                x := 10.
                y := 5.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="Integer" value="10" />
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="y" />
                            <expr>
                                <literal class="Integer" value="5" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_inheritance():
    input = """
        class Str : String {}
        class Main : Object {
            run [|
                x := Str2 read.  
            ]
        }
        class Str2 : Str {}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Str" parent="String" />
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector="read">
                                    <expr>
                                        <literal class="class" value="Str2" />
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
            <class name="Str2" parent="Str" />   
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_integer():
    input = """
        class Main : Object {
            run [| 
                x := 10.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="Integer" value="10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_nil():
    input = """
        class Main : Object {
            run [| 
                x := nil.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="Nil" value="nil" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_true():
    input = """
        class Main : Object {
            run [| 
                x := true.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="True" value="true" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_false():
    input = """
        class Main : Object {
            run [| 
                x := false.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="False" value="false" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string():
    input = """
        class Main : Object {
            run [| 
                x := 'a10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_lt():
    input = """
        class Main : Object {
            run [| 
                x := 'a < 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a &lt; 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_gt():
    input = """
        class Main : Object {
            run [| 
                x := 'a > 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a &gt; 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_amp():
    input = """
        class Main : Object {
            run [| 
                x := 'a & 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a &amp; 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_apos():
    input = """
        class Main : Object {
            run [| 
                x := 'a \\\' 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a \\&apos; 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_quot():
    input = """
        class Main : Object {
            run [| 
                x := 'a " 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a &quot; 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_esc_nl():
    input = """
        class Main : Object {
            run [| 
                x := 'a \\n 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a \\n 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_string_esc_backslash():
    input = """
        class Main : Object {
            run [| 
                x := 'a \\\\ 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <literal class="String" value="a \\\\ 10" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_nested_expr():
    input = """
        class Main : Object {
            run [| 
                x := (((1))).
            ]
        }
        """
    
    exp_output = """
    <?xml version='1.0' encoding='UTF-8'?>
    <program language="SOL25">
        <class name="Main" parent="Object">
            <method selector="run">
                <block arity="0">
                    <assign order="1">
                        <var name="x" />
                        <expr>
                            <literal value="1" class="Integer" />
                        </expr>
                    </assign>
                </block>
            </method>
        </class>
    </program>
    """
    run_valid_test(input, exp_output)

def test_literal_class_new():
    input = """
        class Main : Object {
            run [| 
                x := Integer new.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector ="new">
                                    <expr>
                                        <literal class="class" value="Integer" />
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_literal_class_from():
    input = """
        class Main : Object {
            run [| 
                x := Integer from: 1.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector ="from:">
                                    <expr>
                                        <literal class="class" value="Integer" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="1" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_assign_block():
    input = """
        class Main : Object {
            run [| 
                x := [|].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <block arity="0" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_assign_block_param():
    input = """
        class Main : Object {
            run [| 
                x := [:x|].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <block arity="1">
                                    <parameter order="1" name="x" />
                                </block>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_assign_var():
    input = """
        class Main : Object {
            run [| 
                y := 1.
                x := y.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="y" />
                            <expr>
                                <literal class="Integer" value="1" />
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="x" />
                            <expr>
                                <var name="y" />
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)


def test_block_usage():
    input = """
        class Main : Object {
            run [|
                "a = instance 14"
                a := self foo: 4.
                "b = instance Block"
                b := [ :x | _ := 42. ].
                "c = instance 42"
                c := b value: 16.
                "d = instance 'ahoj' - print vrací self, viz Vestavěné třídy"
                d := 'ahoj' print.
            ]
            foo: [ :x |
            "s proměnnou 'u' se nijak dál nepracuje , ale výsledek zaslání
            zprávy 'plus:' bude vrácen jako výsledek volání metody 'foo'"
                u := x plus: 10.
            ]
        }
    """
    exp_output = """
    <?xml version="1.0" encoding="UTF-8"?>
    <program language="SOL25" description="a = instance 14">
        <class name="Main" parent="Object">
            <method selector="run">
                <block arity="0">
                    <assign order="1">
                        <var name="a"/>
                        <expr>
                            <send selector="foo:">
                                <expr>
                                    <var name="self"/>
                                </expr>
                                <arg order="1">
                                    <expr>
                                        <literal class="Integer" value="4"/>
                                    </expr>
                                </arg>
                            </send>
                        </expr>
                    </assign>
                    <assign order="2">
                        <var name="b"/>
                        <expr>
                            <block arity="1">
                                <parameter name="x" order="1"/>
                                <assign order="1">
                                    <var name="_"/>
                                    <expr>
                                        <literal class="Integer" value="42"/>
                                    </expr>
                                </assign>
                            </block>
                        </expr>
                    </assign>
                    <assign order="3">
                        <var name="c"/>
                        <expr>
                            <send selector="value:">
                                <expr>
                                    <var name="b"/>
                                </expr>
                                <arg order="1">
                                    <expr>
                                        <literal class="Integer" value="16"/>
                                    </expr>
                                </arg>
                            </send>
                        </expr>
                    </assign>
                    <assign order="4">
                        <var name="d"/>
                        <expr>
                            <send selector="print">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </send>
                        </expr>
                    </assign>
                </block>
            </method>
            <method selector="foo:">
                <block arity="1">
                    <parameter name="x" order="1"/>
                    <assign order="1">
                        <var name="u"/>
                        <expr>
                            <send selector="plus:">
                                <expr>
                                    <var name="x"/>
                                </expr>
                                <arg order="1">
                                    <expr>
                                        <literal class="Integer" value="10"/>
                                    </expr>
                                </arg>
                            </send>
                        </expr>
                    </assign>
                </block>
            </method>
        </class>
    </program>
    """
    run_valid_test(input, exp_output)

def test_expr1():
    input = """
        class Main : Object {
            run [| 
                x := (((Integer from: ((Integer new))))).
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector="from:">
                                    <expr>
                                        <literal class="class" value="Integer" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <send selector="new">
                                                <expr>
                                                    <literal class="class" value="Integer" />
                                                </expr>
                                            </send>
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_expr2():
    input = """
        class Main : Object {
            run [| 
                x := (((Integer from: ((Integer new))) plus: (Integer new))).
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector="plus:">
                                    <expr>
                                        <send selector="from:">
                                            <expr>
                                                <literal class="class" value="Integer" />
                                            </expr>
                                            <arg order="1">
                                                <expr>
                                                    <send selector="new">
                                                        <expr>
                                                            <literal class="class" value="Integer" />
                                                        </expr>
                                                    </send>
                                                </expr>
                                            </arg>
                                        </send>
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <send selector="new">
                                                <expr>
                                                    <literal class="class" value="Integer" />
                                                </expr>
                                            </send>
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_expr3():
    input = """
        class Main : Object {
            run [| 
                x := [|
                    x := 2.
                ].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <block arity="0">
                                    <assign order="1">
                                        <var name="x" />
                                        <expr>
                                            <literal class="Integer" value="2" />
                                        </expr>
                                    </assign>
                                </block>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_expr4():
    input = """
        class Main : Object {
            run [| 
                x := ([|
                    x := (2).
                ]).
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <block arity="0">
                                    <assign order="1">
                                        <var name="x" />
                                        <expr>
                                            <literal class="Integer" value="2" />
                                        </expr>
                                    </assign>
                                </block>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)

def test_example():
    input = """
        class Main : Object {
            run "<- definice metody - bezparametrický selektor run"
            [ |
                x := self compute: 3 and: 2 and: 5.
                x := self plusOne: (self vysl).
                y := x asString .
            ]
            
            plusOne: 
            [ :x | 
                r := x plus: 1. 
            ]
            
            compute:and:and: 
            [ :x :y :z |    
                a := x plus: y.
                _ := self vysl: a.
                _ := (( self vysl) greaterThan: 0)
                ifTrue: [|u := self vysl: 1.]
                ifFalse: [|].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="&lt;- definice metody - bezparametrický selektor run">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector="compute:and:and:">
                                    <expr>
                                        <var name="self" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="3" />
                                        </expr>
                                    </arg>
                                    <arg order="2">
                                        <expr>
                                            <literal class="Integer" value="2" />
                                        </expr>
                                    </arg>
                                    <arg order="3">
                                        <expr>
                                            <literal class="Integer" value="5" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="x" />
                            <expr>
                                <send selector="plusOne:">
                                    <expr>
                                        <var name="self" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <send selector="vysl">
                                                <expr>
                                                    <var name="self" />
                                                </expr>
                                            </send>
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="3">
                            <var name="y" />
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="x" />
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>

                <method selector="plusOne:">
                    <block arity="1">
                        <parameter order="1" name="x" />
                        <assign order="1">
                            <var name="r" />
                            <expr>
                                <send selector="plus:">
                                    <expr>
                                        <var name="x" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="1" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>

                <method selector="compute:and:and:">
                    <block arity="3">
                        <parameter order="1" name="x" />
                        <parameter order="2" name="y" />
                        <parameter order="3" name="z" />
                        <assign order="1">
                            <var name="a" />
                            <expr>
                                <send selector="plus:">
                                    <expr>
                                        <var name="x" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <var name="y" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="_" />
                            <expr>
                                <send selector="vysl:">
                                    <expr>
                                        <var name="self" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <var name="a" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="3">
                            <var name="_" />
                            <expr>
                                <send selector="ifTrue:ifFalse:">
                                    <expr>
                                        <send selector="greaterThan:">
                                            <expr>
                                                <send selector="vysl">
                                                    <expr>
                                                        <var name="self" />
                                                    </expr>
                                                </send>
                                            </expr>
                                            <arg order="1">
                                                <expr>
                                                    <literal class="Integer" value="0" />
                                                </expr>
                                            </arg>
                                        </send>
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <block arity="0">
                                                <assign order="1">
                                                    <var name="u" />
                                                    <expr>
                                                        <send selector="vysl:">
                                                        <expr>
                                                            <var name="self" />
                                                        </expr>
                                                        <arg order="1">
                                                            <expr>
                                                                <literal class="Integer" value="1" />
                                                            </expr>
                                                        </arg>
                                                        </send>
                                                    </expr>
                                                </assign>
                                            </block>
                                        </expr>
                                    </arg>
                                    <arg order="2">
                                        <expr>
                                            <block arity="0" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output)
