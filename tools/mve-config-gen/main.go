package main

import "fmt"

var gameClasses = map[string]string{
	GameName_Assault:    "Botpack.Assault",
	GameName_CTF:        "Botpack.CTFGame",
	GameName_DM:         "Botpack.DeathMatchPlus",
	GameName_TDM:        "Botpack.TeamGamePlus",
	GameName_Domination: "Botpack.Domination",
	GameName_LMS:        "Botpack.LastManStanding",
	GameName_BT:         "BTPlusPlusPublicUTBT_beta3.BunnyTrackGame",
	GameName_MH:         "MonsterHunt.MonsterHunt",
	GameName_MA:         "MonsterHunt.MonsterArena",
}

func main() {
	fmt.Println("Hello")
	gameTypes := []string{
		buildLine(GameName_Assault, "Normal", Mutator_Normal, "as"),
		buildLine(GameName_Assault, "InstaGib", Mutator_InstaGib, "as"),
		buildLine(GameName_CTF, "Normal", Mutator_Normal, "ctf"),
		buildLine(GameName_CTF, "InstaGib", Mutator_InstaGib, "ctf"),
		buildLine(GameName_DM, "Normal", Mutator_Normal, "dm"),
		buildLine(GameName_DM, "InstaGib", Mutator_InstaGib, "dm"),
		buildLine(GameName_TDM, "Normal", Mutator_Normal, "dm"),
		buildLine(GameName_TDM, "InstaGib", Mutator_InstaGib, "dm"),
		buildLine(GameName_Domination, "Normal", Mutator_Normal, "dom"),
		buildLine(GameName_Domination, "InstaGib", Mutator_InstaGib, "dom"),
		buildLine(GameName_LMS, "Normal", Mutator_Normal, "lms"),
		buildLine(GameName_LMS, "InstaGib", Mutator_InstaGib, "lms"),
		buildLine(GameName_BT, "Normal", Mutator_BT, "bt"),
		buildLine(GameName_MH, "Normal", Mutator_Normal, "mh"),
		buildLine(GameName_MA, "Normal", Mutator_Normal, "ma"),
	}
	for i, gameTypeString := range gameTypes {
		fmt.Printf("CustomGame[%d]=%s\n", i, gameTypeString)
	}
	for i := len(gameTypes); i < 100; i++ {
		fmt.Printf("CustomGame[%d]=%s\n", i, getDisabledLine())
	}
}

func buildLine(gameName string, ruleName string, mutator string, filterCode string) string {
	return fmt.Sprintf(`(bEnabled=True,GameName="%s",RuleName="%s",GameClass="%s",FilterCode="%s",bHasRandom=True,VotePriority=1.000000,MutatorList="%s",Settings="",Packages="",TickRate=0,ServerActors="",bAvoidRandom=False)`,
		gameName, ruleName, gameClasses[gameName], filterCode, mutator,
	)
}

func getDisabledLine() string {
	return `(bEnabled=False,GameName="",RuleName="",GameClass="",FilterCode="",bHasRandom=False,VotePriority=1.000000,MutatorList="",Settings="",Packages="",TickRate=0,ServerActors="",bAvoidRandom=False)`
}

const (
	GameName_Assault    string = "Assault"
	GameName_CTF        string = "Capture the Flag"
	GameName_DM         string = "Deathmatch"
	GameName_TDM        string = "Team Deathmatch"
	GameName_Domination string = "Domination"
	GameName_LMS        string = "Last Man Standing"
	GameName_BT         string = "BunnyTrack"
	GameName_MH         string = "MonsterHunt"
	GameName_MA         string = "MonsterArena"
)

const (
	Mutator_Normal   string = ""
	Mutator_InstaGib string = "Botpack.InstaGibDM"
	Mutator_BT       string = "BTPlusPlusPublicUTBT_beta3.BTPlusPlus"
)
