<table>
    <tr>
        <th>Opcode</th>
        <th colspan="3">Bit flags</th>
    </tr>
    <tr>
        <th></th>
        <th>a</th>
        <th>d</th>
        <th>*a</th>
    </tr>
    <tr>
        <th>(blank)</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>A =</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>D =</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>*A =</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
    </tr>
    <tr>
        <th>A, D =</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>D, *A =</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
    </tr>
    <tr>
        <th>A, D, *A =</th>
        <th>1</th>
        <th>1</th>
        <th>1</th>
    </tr>
</table>
<br>
<table>
    <tr>
        <th>Opcode</th>
        <th colspan="5">Bit flags</th>
    </tr>
    <tr>
        <th></th>
        <th>u</th>
        <th>op1</th>
        <th>op0</th>
        <th>zx</th>
        <th>sw</th>
    </tr>
    <tr>
        <th>D+A</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>D-A</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>A-D</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
    </tr>
    <tr>
        <th>D+1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>A+1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
    </tr>
    <tr>
        <th>D-1</th>
        <th>1</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>A-1</th>
        <th>1</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
    </tr>
    <tr>
        <th>-D</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
    </tr>
    <tr>
        <th>-A</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>-1</th>
        <th>1</th>
        <th>1</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>D</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
    </tr>
    <tr>
        <th>A</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>D&A</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>D|A</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>~D</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>~A</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
        <th>1</th>
    </tr>
    <tr>
        <th>0</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
    </tr>
</table>

<br>

<table>
    <tr>
        <th>Opcode</th>
        <th colspan="3">Bit flags</th>
    </tr>
    <tr>
        <th></th>
        <th>lt</th>
        <th>eq</th>
        <th>gt</th>
    </tr>
    <tr>
        <th>(blank)</th>
        <th>0</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>; JLT</th>
        <th>1</th>
        <th>0</th>
        <th>0</th>
    </tr>
    <tr>
        <th>; JEQ</th>
        <th>0</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>; JGT</th>
        <th>0</th>
        <th>0</th>
        <th>1</th>
    </tr>
    <tr>
        <th>; JLE</th>
        <th>1</th>
        <th>1</th>
        <th>0</th>
    </tr>
    <tr>
        <th>; JGE</th>
        <th>0</th>
        <th>1</th>
        <th>1</th>
    </tr>
    <tr>
        <th>; JMP</th>
        <th>1</th>
        <th>1</th>
        <th>1</th>
    </tr>
</table>