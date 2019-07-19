' Credits RTSoft Team
'   RasyidMF as Coding
'   KochengAbuOren as Design
' Please dont remove the credits if you using our Source code / Application :D

Public Class Home
    Dim Sys32Loc As String = Environment.SystemDirectory
    Private Function ShellNet(ByVal System32Location As String, ByVal Command As String) As String
        Dim OP As New Process()
        Dim OStartInfo As New ProcessStartInfo(System32Location & "\netsh.exe", Command)
        OStartInfo.UseShellExecute = False
        OStartInfo.CreateNoWindow = True
        OStartInfo.RedirectStandardOutput = True
        OP.StartInfo = OStartInfo
        OP.Start()

        Dim Output As String
        Using SR As System.IO.StreamReader = OP.StandardOutput
            Output = SR.ReadToEnd()
        End Using
        Return Output
    End Function
    Private Function SplitAndGetResult(ByVal Content As String, ByVal SplitString As String, ByVal Index As Integer)
        Dim Explode As String() = Split(Content, SplitString)
        Dim Result As String = Nothing
        Try
            Dim Result_Temp As String() = Split(Explode(Index), vbNewLine)
            Result = Result_Temp(0)
        Catch EX As Exception
            Result = ""
        End Try
        Return Result
    End Function
    Private Sub Home_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim Output As String = ShellNet(Sys32Loc, "wlan show profiles")
        Dim Explode As String() = Split(Output, "    All User Profile     : ")

        Dim iDX As Integer = 0
        Try
            Do
                iDX += 1
                ListBox1.Items.Add("-> " & Explode(iDX).Replace(vbNewLine, ""))
            Loop While True
        Catch : End Try
    End Sub

    Private Sub ListBox1_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ListBox1.SelectedIndexChanged
        Dim Exp As String() = Split(ListBox1.SelectedItem, "-> ")
        Dim ShellResult As String = ShellNet(Sys32Loc, "wlan show profile name=""" & Exp(1) & """ key=clear")

        TextBox1.Text = SplitAndGetResult(ShellResult, "Version                : ", 1)
        TextBox2.Text = SplitAndGetResult(ShellResult, "Type                   : ", 1)
        TextBox3.Text = SplitAndGetResult(ShellResult, " Name                   : ", 1)
        TextBox6.Text = SplitAndGetResult(ShellResult, "Number of SSIDs        : ", 1)
        TextBox5.Text = Exp(1)
        TextBox4.Text = SplitAndGetResult(ShellResult, "Network type           : ", 1)
        TextBox7.Text = SplitAndGetResult(ShellResult, "Radio type             : ", 1)
        TextBox8.Text = SplitAndGetResult(ShellResult, "Vendor extension          : ", 1)
        TextBox11.Text = SplitAndGetResult(ShellResult, "Authentication         : ", 1)
        TextBox10.Text = SplitAndGetResult(ShellResult, "Cipher                 : ", 1)
        TextBox9.Text = SplitAndGetResult(ShellResult, "Authentication         : ", 2)
        TextBox12.Text = SplitAndGetResult(ShellResult, "Cipher                 : ", 2)
        TextBox13.Text = SplitAndGetResult(ShellResult, "Security key           : ", 1)
        TextBox14.Text = SplitAndGetResult(ShellResult, "Key Content            : ", 1)
        TextBox17.Text = SplitAndGetResult(ShellResult, "Cost                   : ", 1)
        TextBox16.Text = SplitAndGetResult(ShellResult, "Congested              : ", 1)
        TextBox15.Text = SplitAndGetResult(ShellResult, "Approaching Data Limit : ", 1)
        TextBox18.Text = SplitAndGetResult(ShellResult, "Over Data Limit        : ", 1)
        TextBox19.Text = SplitAndGetResult(ShellResult, "Roaming                : ", 1)
        TextBox20.Text = SplitAndGetResult(ShellResult, "Cost Source            : ", 1)
    End Sub
End Class
