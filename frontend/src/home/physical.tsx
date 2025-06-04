import * as React from "react"
import { useForm } from "react-hook-form"
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
} from "@/components/ui/form"
import { useNavigate } from "react-router-dom"
import { Button } from "@/components/ui/button"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Slider } from "@/components/ui/slider"

export default function Physical() {
  const navigate = useNavigate()

  // Initialize the form with default values
  const form = useForm({
    defaultValues: {
      n_cores: "1",
      file_topology: "dt_backbone",
      traffic_lambda: "0.0025",
      traffic_conn_types: "48",
      fiber_allocation: "random_fit",
      modulation: "64-QAM",
      min_load: 100,
      max_load: 500,
      load_interval: 100,
    },
  })

  // POST METHOD PARA ENVIO DOS DADOS PARA O BACKEND!!!!(Precisamos de mais testes)
  async function onSubmit(values) {
    // Gera os pontos de carga para enviar ao backend
    const loads = []
    for (
      let i = Number(values.min_load);
      i <= Number(values.max_load);
      i += Number(values.load_interval)
    ) {
      loads.push(i)
    }
    const payload = { ...values, loads }
  
    try {
      const response = await fetch("/api/physical-config", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      })
  
      if (!response.ok) {
        throw new Error("Erro ao enviar dados para o backend")
      }
  
      // Se quiser tratar a resposta:
      // const data = await response.json()
      // console.log(data)
  
      navigate("/network")
    } catch (error) {
      alert("Erro ao enviar dados para o backend: " + error.message)
    }
  }
  

  // Para a barra de range (visualização)
  const minLoad = form.watch("min_load")
  const maxLoad = form.watch("max_load")
  const loadInterval = form.watch("load_interval")
  const loadPoints = []
  for (
    let i = Number(minLoad);
    i <= Number(maxLoad);
    i += Number(loadInterval)
  ) {
    loadPoints.push(i)
  }

  // Garante que min_load nunca seja maior que max_load e vice-versa
  React.useEffect(() => {
    if (minLoad > maxLoad) {
      form.setValue("min_load", maxLoad)
    }
    if (maxLoad < minLoad) {
      form.setValue("max_load", minLoad)
    }
  }, [minLoad, maxLoad, form])

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-4">Physical Configuration</h1>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            name="n_cores"
            control={form.control}
            rules={{ required: "Number of cores is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Number of Cores</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select number of cores" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="1">1</SelectItem>
                    <SelectItem value="2">2</SelectItem>
                    <SelectItem value="7">7</SelectItem>
                  </SelectContent>
                </Select>
                <FormDescription>
                  Select the number of cores for simulation.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="file_topology"
            control={form.control}
            rules={{ required: "Topology is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Network Topology</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select topology" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="dt_backbone">DT Backbone</SelectItem>
                    <SelectItem value="nsfnet">NSFNet</SelectItem>
                    <SelectItem value="ring-4">Ring-4</SelectItem>
                  </SelectContent>
                </Select>
                <FormDescription>
                  Select the network topology to simulate.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="traffic_lambda"
            control={form.control}
            rules={{ required: "Traffic lambda is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Traffic Lambda</FormLabel>
                <FormControl>
                  <input
                    type="number"
                    step="0.0001"
                    placeholder="Enter traffic lambda"
                    {...field}
                  />
                </FormControl>
                <FormDescription>
                  Enter the traffic lambda value (default: 0.0025).
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="traffic_conn_types"
            control={form.control}
            rules={{ required: "Connection type is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Connection Type (Gbps)</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select connection type" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="48">48 Gbps</SelectItem>
                    <SelectItem value="120">120 Gbps</SelectItem>
                    <SelectItem value="240">240 Gbps</SelectItem>
                    <SelectItem value="480">480 Gbps</SelectItem>
                    <SelectItem value="1200">1200 Gbps</SelectItem>
                  </SelectContent>
                </Select>
                <FormDescription>
                  Select the connection type in Gbps.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="fiber_allocation"
            control={form.control}
            rules={{ required: "Fiber allocation is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Fiber Allocation</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select fiber allocation" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="random_fit">Random Fit</SelectItem>
                    <SelectItem value="first_fit">First Fit</SelectItem>
                  </SelectContent>
                </Select>
                <FormDescription>
                  Select the fiber allocation strategy.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="modulation"
            control={form.control}
            rules={{ required: "Modulation is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Modulation</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select modulation" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="64-QAM">64-QAM</SelectItem>
                    <SelectItem value="32-QAM">32-QAM</SelectItem>
                    <SelectItem value="16-QAM">16-QAM</SelectItem>
                    <SelectItem value="8-QAM">8-QAM</SelectItem>
                    <SelectItem value="4-QAM">4-QAM</SelectItem>
                  </SelectContent>
                </Select>
                <FormDescription>
                  Select the modulation scheme.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Sliders para carga mínima e máxima */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FormField
              name="min_load"
              control={form.control}
              rules={{ required: "Carga mínima obrigatória" }}
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Carga Mínima</FormLabel>
                  <FormControl>
                    <div className="flex flex-col gap-2">
                      <Slider
                        min={100}
                        max={500}
                        step={1}
                        value={[Number(field.value)]}
                        onValueChange={([val]) => {
                          // Garante que min_load nunca seja maior que max_load
                          if (val > maxLoad) {
                            form.setValue("max_load", val)
                          }
                          field.onChange(val)
                        }}
                      />
                      <span className="text-sm text-muted-foreground">
                        {minLoad}
                      </span>
                    </div>
                  </FormControl>
                  <FormDescription>
                    Selecione a carga mínima (100 a 500)
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              name="max_load"
              control={form.control}
              rules={{ required: "Carga máxima obrigatória" }}
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Carga Máxima</FormLabel>
                  <FormControl>
                    <div className="flex flex-col gap-2">
                      <Slider
                        min={100}
                        max={500}
                        step={1}
                        value={[Number(field.value)]}
                        onValueChange={([val]) => {
                          // Garante que max_load nunca seja menor que min_load
                          if (val < minLoad) {
                            form.setValue("min_load", val)
                          }
                          field.onChange(val)
                        }}
                      />
                      <span className="text-sm text-muted-foreground">
                        {maxLoad}
                      </span>
                    </div>
                  </FormControl>
                  <FormDescription>
                    Selecione a carga máxima (100 a 500)
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>

          {/* Campo para intervalo */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FormField
              name="load_interval"
              control={form.control}
              rules={{ required: "Intervalo obrigatório" }}
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Intervalo</FormLabel>
                  <FormControl>
                    <input
                      type="number"
                      min={1}
                      max={Math.max(1, maxLoad - minLoad)}
                      step={1}
                      {...field}
                    />
                  </FormControl>
                  <FormDescription>
                    Intervalo entre cargas (ex: 100)
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>

          {/* Visualização dos pontos de carga */}
          <div className="my-4">
            <FormLabel>Pontos de carga selecionados:</FormLabel>
            <div className="flex gap-2 mt-2 flex-wrap">
              {loadPoints.map((val) => (
                <span
                  key={val}
                  className="px-2 py-1 bg-blue-100 rounded text-blue-800 text-sm"
                >
                  {val}
                </span>
              ))}
            </div>
          </div>

          <Button type="submit">Next: Network Configuration</Button>
        </form>
      </Form>
    </div>
  )
}
