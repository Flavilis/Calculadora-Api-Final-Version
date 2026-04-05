document.querySelector("button").addEventListener("click", async () => {
    const num1 = document.querySelector("input[name='num1']").value;
    const num2 = document.querySelector("input[name='num2']").value;
    const operacao = document.getElementById("operacao").value;

    try {
        const response = await fetch(`http://127.0.0.1:8000/${operacao}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ numero1: parseFloat(num1), numero2: parseFloat(num2) })
        });

        if (!response.ok) {
            const error = await response.json();
            document.getElementById("resultado").textContent = `Erro: ${error.detail}`;
            return;
        }

        const data = await response.json();
        document.getElementById("resultado").textContent = data.resultado;
    } catch (err) {
        document.getElementById("resultado").textContent = "Erro de conexão com a API";
    }
});
