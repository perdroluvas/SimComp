/*Pagina para parametros de camada de Rede*/
import * as React from "react";
import './parameters.css';
import {useFormContext} from 'react-hook-form';
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
  } from "@/components/ui/dropdown-menu"
import { Card} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import {
    FormControl,
    FormField,
    FormItem,
  } from "@/components/ui/form";
  

export default function Networking() {
    const {register,control}= useFormContext({
        defaultValue:{
            Modulations:[],
            options:[],
            BitRate:[],
        }
    });
    return (
        <main className="pt-6 pl-4 pr-4 pb-8">
            <Card className="sm:col-span-2" x-chunk="dashboard-05-chunk-0">
                <div className="grid w-full items-start gap-6">
                    <fieldset className="grid gap-6 rounded-lg border p-4">
                        <div className="grid gap-3">
                            <Label htmlFor="model">insert variable data</Label>
                        </div>
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid gap-3">
                                <FormField
                                control={control}
                                name="Network_Topology"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="Network_Topology">Network Topology</Label>
                                <Select onValueChange={field.onChange} defaultValue="Network_Topology">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select a option" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                    <SelectItem value="dt">dt</SelectItem>
                                    <SelectItem value="nsfnet">nsfnet</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <Label htmlFor="Guard Band">Guard Band</Label>
                                <Input className='input' {...register("Guard_Band")}  type="number" placeholder="1" min="1" />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <FormField
                                control={control}
                                name="N_cores_MCF"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="N_cores_MCF">MCF's number of cores</Label>
                                <Select onValueChange={field.onChange} defaultValue="N_cores_MCF">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select a option" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                    <SelectItem value="1">1</SelectItem>
                                    <SelectItem value="7">7</SelectItem>
                                    <SelectItem value="12">12</SelectItem>
                                    <SelectItem value="19">19</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                            <DropdownMenu>
                            <DropdownMenuTrigger asChild className="input"> 
                            <Button variant="outline">Max.Modulation</Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent className="w-56">
                            <DropdownMenuLabel>Modulations</DropdownMenuLabel>
                            <DropdownMenuSeparator />
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input  type="checkbox" value="4" {...register("Modulation")} />
                                    4DP-QAM
                                </label>
                                </div>
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="8" {...register("Modulation")} />
                                    8DP-QAM
                                </label>
                                </div>
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="16" {...register("Modulation")} />
                                    16DP-QAM
                                </label>
                                </div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="32" {...register("Modulation")}  />
                                    32DP-QAM
                                </label>
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="64" {...register("Modulation")}  />
                                    64DP-QAM
                                </label>
                                </div>
                            </DropdownMenuContent>
                            </DropdownMenu>
                            </div>
                            </div>
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid gap-3">
                                <Label htmlFor="Span Length">Span Length (km)</Label>
                                <Input className='input' {...register("Span_Length")} type="number" placeholder="80" min="80" max="100" />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                            <DropdownMenu>
                            <DropdownMenuTrigger asChild className="input"> 
                            <Button variant="outline">BitRate</Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent className="w-56">
                            <DropdownMenuLabel>BitRate</DropdownMenuLabel>
                            <DropdownMenuSeparator />
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input  type="checkbox" value="48" {...register("BitRate")} />
                                    48 Gb/s
                                </label>
                                </div>
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="120" {...register("BitRate")} />
                                    120 Gb/s
                                </label>
                                </div>
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="240" {...register("BitRate")} />
                                    240 Gb/s
                                </label>
                                </div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="480" {...register("BitRate")}  />
                                    480 Gb/s
                                </label>
                                <div>
                                <label className="relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50">
                                    <input type="checkbox" value="1200" {...register("BitRate")}  />
                                    1200 Gb/s
                                </label>
                                </div>
                            </DropdownMenuContent>
                            </DropdownMenu>
                            </div>
                        </div>
                            </div>
                    </fieldset>
                    <fieldset className="grid gap-6 rounded-lg border p-4">
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid gap-3">
                                <FormField
                                control={control}
                                name="Routing"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="Routing">Routing</Label>
                                <Select onValueChange={field.onChange} defaultValue="Routing">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select a option" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                    <SelectItem value="first_fit">first fit</SelectItem>
                                    <SelectItem value="random_fit">random fit</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <FormField
                                control={control}
                                name="Fiber_allocation"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="Fiber_allocation">Fiber allocation</Label>
                                <Select onValueChange={field.onChange} defaultValue="Fiber_allocation">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select a option" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                    <SelectItem value="first_fit">first fit</SelectItem>
                                    <SelectItem value="random_fit">random fit</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                        </div>
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid gap-3">
                                <FormField
                                control={control}
                                name="Type_Core_selection"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="Type_Core_selection">Type Core selection</Label>
                                <Select onValueChange={field.onChange} defaultValue="Type_Core_selection">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select a option" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                    <SelectItem value="first_fit">first fit</SelectItem>
                                    <SelectItem value="random_fit">random fit</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                            </div>
                            </div>
                    </fieldset>
                    
                </div>
            </Card>
        </main>
    )
}
