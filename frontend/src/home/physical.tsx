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
} from "@/components/ui/form" // Adjust the import path as needed
import { useNavigate } from "react-router-dom"
import { Button } from "@/components/ui/button"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

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
    },
  })

  // Handle form submission
  function onSubmit(values) {
    console.log(values)
    navigate("/network")
  }

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
                <FormDescription>Select the number of cores for simulation.</FormDescription>
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
                <FormDescription>Select the network topology to simulate.</FormDescription>
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
                <FormDescription>Enter the traffic lambda value (default: 0.0025).</FormDescription>
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
                <FormDescription>Select the connection type in Gbps.</FormDescription>
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
                <FormDescription>Select the fiber allocation strategy.</FormDescription>
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
                <FormDescription>Select the modulation scheme.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <Button type="submit">Next: Network Configuration</Button>
        </form>
      </Form>
    </div>
  )
}