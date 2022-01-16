package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"sync"
	"time"
)

func main() {
	http.HandleFunc("/sendTC", sendTcHandler)
	http.HandleFunc("/assin_task", assin_task)
	http.ListenAndServe(":8080", nil)
}

func sendTcHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("run sendTC... url->", r.RequestURI)

	r.ParseMultipartForm(1024)
	tc_param := r.PostForm
	log.Printf("tc_param: %v, %T", tc_param, tc_param)
	_, err := http.PostForm("http://127.0.0.1:8080/assin_task", tc_param)
	if err != nil {
		log.Fatalln(err)
	}

	res_map := map[string]string{"status": "success", "time": time.Now().GoString()}
	res_byteArray, _ := json.Marshal(res_map)
	fmt.Fprintf(w, string(res_byteArray))
}

func assin_task(w http.ResponseWriter, r *http.Request) {
	log.Println("run assin_task... url->", r.RequestURI)

	r.ParseForm()
	log.Printf("http PostForm: %v, %T\n", r.PostForm["param"], r.PostForm["param"][0])
	var msg map[string][]map[string]string
	err := json.Unmarshal([]byte(r.PostForm["param"][0]), &msg)
	if err != nil {
		log.Fatalln(err)
	}
	testcases_num := len(msg["testcases"])
	var wg sync.WaitGroup
	wg.Add(testcases_num)
	for i := 0; i < testcases_num; i++ {
		log.Println(msg["testcases"][i])
		go run_task(&wg, msg["testcases"][i], r.PostForm["username"][0])
	}
}

func run_task(wg *sync.WaitGroup, p_params map[string]string, username string) {
	log.Println("run run_task")
	log.Println(p_params)
	time.Sleep(360 * time.Second)
	log.Println(p_params)

	fileName := p_params["executeParam"] + username + filepath.Ext(filepath.Clean(p_params["scriptPath"]))
	fullfileName := filepath.Join(filepath.Clean("F:/code_go/src/code_study/chap_06/demo08/"), fileName)
	data, err := json.Marshal(p_params)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(fullfileName)
	f, err := os.Create(fullfileName)
	if err != nil {
		log.Fatalln(err)
	}
	f.WriteString(string(data))
	f.Close()
	wg.Done()
}
