import wx, os, pygame

asd = 1

def cz(sr):
    fp = open("Romance of the three kingdoms.txt", "r", encoding="utf-8")
    sample = fp.readlines()
    count = len(sample)
    bz = 0
    i = 0
    while i < count:
        fc = []
        for s in sample[i]:
            fc.append(s)
        j = 0
        while j < len(fc):
            if sr == fc[j]:
                bz = 1
                break
            else:
                j += 1
        if bz == 1:
            break
        else:
            i += 1
    fp.close()
    return i, j


def ewuy(qh, b, z):
    uy = open("A dream of red mansions.txt", "r", encoding="utf-8")
    po = uy.readlines()
    wil = 0
    pu = ''
    rey = ''
    while b >= 0:
        while z >= 0:
            pu = po[b]
            rey = pu[z]
            if qh == rey:
                wil += 1
            z -= 1
        b -= 1
        z = len(po[b])
        z -= 1
    uy.close()
    return wil


def th(s, w, ds):
    sc = open("A dream of red mansions.txt", "r", encoding="utf-8")
    lg = sc.readlines()
    jh = lg[s]
    eu = jh[w]
    kuy = ewuy(eu, s, w)
    if eu != '原' and kuy != 699:
        ud = str(kuy)

        orh = eu + ud
        sc.close()
        return orh
    else:
        ds += "*"
        return ds


def jiemizhe(feh):
    qwe = 0
    hfd = ""
    while qwe < len(feh):
        if feh[qwe] < '\u4e00' or '\u9fff' < feh[qwe]:
            dfs = feh[qwe]
            qwe += 1
            hfd += dfs
        else:
            x, y = cz(feh[qwe])
            aik = th(x, y, feh[qwe])
            qwe += 1
            hfd += aik
    return hfd


class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        self.Frame = wx.Frame(parent=None,
                              title="加密者",
                              pos=(100, 100),
                              size=(768, 543))
        self.Frame.SetMaxSize((768, 543))
        self.Frame.SetMinSize((768, 543))
        self.SetTopWindow(self.Frame)
        self.panel = wx.Panel(self.Frame, -1)
        self.Set_Button()
        self.Set_Test_Ctrl()
        self.Set_Image()
        self.Frame.Show()
        return True

    def Set_Button(self):
        self.button1 = wx.Button(self.panel,
                                 -1,
                                 "确定",
                                 pos=(180, 380),
                                 size=(100, 40))
        font1 = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.button1.SetFont(font1)
        self.Bind(wx.EVT_BUTTON, self.OnclickSubmit, self.button1)
        self.button2 = wx.Button(self.panel,
                                 -1,
                                 "取消",
                                 pos=(480, 380),
                                 size=(100, 40))
        font2 = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.button2.SetFont(font2)
        self.Bind(wx.EVT_BUTTON, self.OnclickCancle, self.button2)

    def Set_Test_Ctrl(self):
        self.inputext2 = wx.TextCtrl(self.panel,
                                     -1,
                                     "",
                                     pos=(260, 200),
                                     size=(360, 40))
        font2 = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.inputext2.SetFont(font2)

        self.inputext3 = wx.TextCtrl(self.panel,
                                     -1,
                                     "",
                                     pos=(260, 290),
                                     size=(360, 40))
        font2 = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.inputext3.SetFont(font2)

    def Set_Image(self):
        image_file2 = 'Music label.jpg'
        bmp2 = wx.Image(image_file2, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button4 = wx.BitmapButton(self.panel,
                                       -1,
                                       bmp2,
                                       pos=(40, 40),
                                       size=(60, 60))
        pygame.mixer.init()
        pygame.mixer.music.load("Background music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.pause()
        pygame.mixer.unpause()
        self.button4.Bind(wx.EVT_LEFT_DOWN, self.three_play)

        image_file = 'Encryption program background.jpg'
        bmp = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self.panel, -1, bmp, size=(-1, -1))
        self.button3.Bind(wx.EVT_LEFT_DOWN, self.one_play)

    def OnclickSubmit(self, event):
        message = ""
        username = str(self.inputext2.GetValue())
        fan_hui = jiemizhe(username)
        self.inputext3.SetValue(fan_hui)

    def OnclickCancle(self, event):
        self.inputext2.SetValue("")
        self.inputext3.SetValue("")

    def open_File(self, event):
        file = wx.FileDialog(None, "choose you file", os.getcwd(), "", "",
                             wx.FD_OPEN)
        if file.ShowModal() == wx.ID_OK:
            i = file.GetPath()
            print(i)
            file.Destroy()
            self.inputext.SetLabel(i)

    def one_play(self, event):
        print("")

    def three_play(self, event):
        global asd
        if asd == 0:
            pygame.mixer.music.play(-1)
            pygame.mixer.pause()
            pygame.mixer.unpause()
            asd = 1
        else:
            pygame.mixer.music.stop()
            asd = 0


if __name__ == "__main__":
    MyApp().MainLoop()
